import cv2 as cv
import numpy as np
from . import module as m
import time
import csv



def gaze(frame, face_detector, face_landmarker):
    grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    height, width = grayFrame.shape
    image, face,totalfaces = m.faceDetector(frame, grayFrame, face_detector)
    if(totalfaces<1 or totalfaces>1):
        return None
    if face is not None:
        image, PointList = m.faceLandmakDetector(frame, grayFrame, face,face_landmarker, False)
        RightEyePoint = PointList[36:42]
        LeftEyePoint = PointList[42:48]
        leftRatio, topMid, bottomMid = m.blinkDetector(LeftEyePoint)
        rightRatio, rTop, rBottom = m.blinkDetector(RightEyePoint)
        maskright, rightpos= m.EyeTracking(frame, grayFrame, RightEyePoint)
        maskleft, leftpos = m.EyeTracking(frame, grayFrame, LeftEyePoint)
        return leftpos
