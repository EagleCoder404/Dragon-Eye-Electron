import cv2
import dlib
import numpy as np
import csv

def refine(mask,img, kernel):
    mask = cv2.dilate(mask, kernel, 5)
    eyes = cv2.bitwise_and(img, img, mask=mask)
    mask = (eyes == [0, 0, 0]).all(axis=2)
    eyes[mask] = [255, 255, 255]
    eyes_gray = cv2.cvtColor(eyes, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(eyes_gray, 145, 255, cv2.THRESH_BINARY)
    thresh = cv2.erode(thresh, None, iterations=2) #1
    thresh = cv2.dilate(thresh, None, iterations=4) #2
    thresh = cv2.medianBlur(thresh, 3) #3
    thresh = cv2.bitwise_not(thresh)
    return thresh

def shape_to_np(shape, dtype="int"):
	coords = np.zeros((68, 2), dtype=dtype)
	for i in range(0, 68):
		coords[i] = (shape.part(i).x, shape.part(i).y)
	return coords

def eye_on_mask(mask, side, shape):
    points = [shape[i] for i in side]
    points = np.array(points, dtype=np.int32)
    mask = cv2.fillConvexPoly(mask, points, 255)
    return mask

def face_alignment_detector(img, detector, predictor):
    left = [1,2,3,4,5,49,29,40]
    right = [43,29,55,13,14,15,16]


    kernel = np.ones((9, 9), np.uint8)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 1)

    if(len(rects)<1):
        return None
    elif(len(rects)>1):
        return None
            
    for rect in rects:

        shape = predictor(gray, rect)
        shape = shape_to_np(shape)
        mask_left = np.zeros(img.shape[:2], dtype=np.uint8)
        mask_right = np.zeros(img.shape[:2], dtype=np.uint8)
        
        
        mask_left = eye_on_mask(mask_left, left, shape)
        mask_right = eye_on_mask(mask_right, right, shape)
    
        
        refined_left=refine(mask_left,img, kernel)
        refined_right=refine(mask_right,img, kernel)
        
        refined_left_white_count=np.sum(refined_left==255)
        refined_right_white_count=np.sum(refined_right==255)
        
        message=""
        if((refined_left_white_count-refined_right_white_count)>2200):
            message="left"
        elif((refined_right_white_count-refined_left_white_count)>2200):
            message="right"
        else:
            message="front"

        return message
        
