import time
import cv2
import os
import imutils
import pickle
import sys
from logger import Logger

from proctoring_features.face_recognize import recognize
from proctoring_features.face_align import face_alignment_detector
from proctoring_features.pupil_position import gaze
from proctoring_features.face_box import get_bounding_box

import dlib

token = sys.argv[1]
# initialization
########################################
curr_path = os.getcwd()

proto_path = os.path.join(curr_path, 'facial/model', 'deploy.prototxt')
model_path = os.path.join(curr_path, 'facial/model', 'res10_300x300_ssd_iter_140000.caffemodel')
recognition_model = os.path.join(curr_path, 'facial/model', 'openface_nn4.small2.v1.t7')
face_detector = cv2.dnn.readNetFromCaffe(prototxt=proto_path, caffeModel=model_path)
face_embedder = cv2.dnn.readNetFromTorch(model=recognition_model)
face_recognizer = pickle.loads(open('facial/recognizer.pickle', "rb").read())
face_labeler = pickle.loads(open('facial/le.pickle', "rb").read())
landmarker = dlib.shape_predictor('facial/model/shape_predictor_68_face_landmarks.dat')
hog_detector = dlib.get_frontal_face_detector()
cam = cv2.VideoCapture(0)
print("Data Loaded")
main_log = Logger(f"facial/logs/{token}.log")
########################################



def proctoring_is_on():
    with open(os.getcwd()+"/stop_proctoring_features") as config:
        config_content = config.read()
        if config_content == "false":
            return True
        else:
            return False



def main(frame):
    frame = imutils.resize(frame, width=600)
    
    face_name = None
    multiple_face = None
    face_detected = None
    eye_position = None
    face_alignement = None

    bb = get_bounding_box(frame, face_detector)
    number_of_detected_faces = len(bb)

    if number_of_detected_faces > 1:
        multiple_face = True
    else:
        multiple_face = False

    if bb != [] :
        face_detected = True
    else:
        face_detected = False 

    if face_detected and not multiple_face:
        bb = bb[0]
        face = frame[bb['startY']:bb['endY'], bb["startX"]:bb["endX"]]
        if face.size == 0:
            return
        face_name = recognize(face, face_embedder, face_recognizer, face_labeler)
        if face_name == "You are not suppose to be here":
            face_name = False
        else:
            face_name = True
        face_alignement = face_alignment_detector(frame, hog_detector, landmarker)
        eye_position = gaze(frame, hog_detector, landmarker)[0]
        
    main_log.log([face_detected, multiple_face, face_name, face_alignement, eye_position])
    print([face_detected, multiple_face, face_name, face_alignement, eye_position])
    # cv2.imshow("lol", frame)


# the main loop
while True:
    if not proctoring_is_on():
        break
    ret, frame = cam.read()
    main(frame)
    # time.sleep(0.3)
    # key = cv2.waitKey(1) & 0xFF
    # if key == ord('q'):
    #     break

# cv2.destroyAllWindows()
cam.release()