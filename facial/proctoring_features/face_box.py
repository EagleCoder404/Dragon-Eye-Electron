import cv2
import imutils
import numpy as np
def get_bounding_box(frame, face_detector):
    
    (h, w) = frame.shape[:2]
    image_blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0), False, False)
    face_detector.setInput(image_blob)
    face_detections = face_detector.forward()
    
    max_confidence = 0
    max_confidence_bbox = {}

    for i in range(0, face_detections.shape[2]):
        confidence = face_detections[0, 0, i, 2]
        if confidence >= 0.75 and (confidence > max_confidence):
            box = face_detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            max_confidence_bbox = { "startX":startX, "startY":startY, "endX":endX, "endY":endY , "confidence":confidence}
    return max_confidence_bbox