import time
import os
import cv2
import imutils
import pickle

from proctoring_features.face_recognize import recognize
from proctoring_features.face_align import face_alignment_detector
from proctoring_features.pupil_position import gaze
from proctoring_features.face_box import get_bounding_box

import dlib
# initialization
####################################
curr_path = os.getcwd()
print(curr_path)
proto_path = os.path.join(curr_path, 'facial/model', 'deploy.prototxt')
model_path = os.path.join(curr_path, 'facial/model', 'res10_300x300_ssd_iter_140000.caffemodel')
recognition_model = os.path.join(curr_path, 'facial/model', 'openface_nn4.small2.v1.t7')
face_detector = cv2.dnn.readNetFromCaffe(prototxt=proto_path, caffeModel=model_path)
face_embedder = cv2.dnn.readNetFromTorch(model=recognition_model)
face_recognizer = pickle.loads(open('facial/recognizer.pickle', "rb").read())
face_labeler = pickle.loads(open('facial/le.pickle', "rb").read())
landmarker = dlib.shape_predictor('facial/model/shape_predictor_68_face_landmarks.dat')
hog_detector = dlib.get_frontal_face_detector()
log_file = open("log_file.txt", "a")
print("models loaded")
cam = cv2.VideoCapture(0)
print("camera captured")
####################################



def proctoring_is_on():
    """
        To Check if Proctoring is Turned on, by reading stop_proctoring_features file
    """
    with open(os.getcwd()+"/stop_proctoring_features") as config:
        config_content = config.read()
        if config_content == "false":
            return True
        else:
            return False

def main(cam):
    """
        Add All Procotring Code here
    """
    ret, frame = cam.read()
    frame = imutils.resize(frame, width=600)

    bb = get_bounding_box(frame, face_detector)
    if bb == {}: 
        print("face not detected")
        return
    face = frame[bb['startY']:bb['endY'], bb["startX"]:bb["endX"]]
    if face.size == 0:
        return
    detected_face = recognize(face, face_embedder, face_recognizer, face_labeler)
    face_alignement = face_alignment_detector(frame, hog_detector, landmarker)
    res = gaze(frame, hog_detector, landmarker)

    print("{:<10s} {:<20s} {:<20s}".format(str(detected_face), str(face_alignement), str(res)))


    cv2.imshow("lol", frame)


# the main loop
while True:
    # if not proctoring_is_on():
    #     break
    main(cam)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cv2.destroyAllWindows()
cam.release()