import numpy as np
import cv2
import time
import datetime
import imutils

    
def recognize(face, face_embedder, face_recognizer, face_labeler):
    face_blob = cv2.dnn.blobFromImage(face, 1.0/255, (96, 96), (0, 0, 0), True, False)
    face_embedder.setInput(face_blob)
    vec = face_embedder.forward()
    preds = face_recognizer.predict_proba(vec)[0]
    j = np.argmax(preds)
    proba = preds[j]
    name = face_labeler.classes_[j]
    return name



