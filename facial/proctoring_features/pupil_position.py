import cv2 as cv
import numpy as np
from . import module as m
import time
import csv
# Variables

COUNTER = 0
TOTAL_BLINKS = 0
CLOSED_EYES_FRAME = 3
FRAME_COUNTER = 0

#camera = cv.VideoCapture(0)
def gaze(frame, face_detector, face_landmarker):
    COUNTER = 0
    TOTAL_BLINKS = 0
    CLOSED_EYES_FRAME = 3
    #FRAME_COUNTER = 0



    # converting frame into Gry image.
    grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    height, width = grayFrame.shape
    circleCenter = (int(width/2), 50)
    # calling the face detector funciton
    image, face,totalfaces = m.faceDetector(frame, grayFrame, face_detector)
    if(totalfaces<1 or totalfaces>1):
        return [FRAME_COUNTER,"conflict","conflict"]
    if face is not None:
        image, PointList = m.faceLandmakDetector(frame, grayFrame, face,face_landmarker, False)


        RightEyePoint = PointList[36:42]
        LeftEyePoint = PointList[42:48]
        leftRatio, topMid, bottomMid = m.blinkDetector(LeftEyePoint)
        rightRatio, rTop, rBottom = m.blinkDetector(RightEyePoint)


        blinkRatio = (leftRatio + rightRatio)/2

        if blinkRatio > 4:
            COUNTER += 1
            
        else:
            if COUNTER > CLOSED_EYES_FRAME:
                TOTAL_BLINKS += 1
                COUNTER = 0
        maskright, rightpos= m.EyeTracking(frame, grayFrame, RightEyePoint)
        maskleft, leftpos = m.EyeTracking(frame, grayFrame, LeftEyePoint)
        return [FRAME_COUNTER, leftpos, rightpos]
