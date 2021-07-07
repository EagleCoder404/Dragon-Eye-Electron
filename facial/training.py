import numpy as np
import cv2
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
import pickle
import os
import imutils
import sys
from playsound import playsound
from pathlib import Path

database_path = Path("facial/database")
if not database_path.exists():
    os.mkdir(database_path)
    os.mkdir(database_path / "user")
user_dir = database_path / "user"
for file in os.listdir(user_dir):
    os.remove(user_dir / file)
    

cam=cv2.VideoCapture(0)
counter=0
while True:
    
    ret,frame=cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("Audio guidance",frame)
    if(counter==0):
        
        playsound("facial/audio/front.mp3")
    elif(counter==200):
        
        playsound("facial/audio/right30.mp3")
    elif(counter==400):
        
        playsound("facial/audio/right60.mp3")
    elif(counter==600):
        
        playsound("facial/audio/left30.mp3")
    elif(counter==800):
        
        playsound("facial/audio/left60.mp3")
    elif(counter==1000):
        
        playsound("facial/audio/front30up.mp3")
    elif(counter==1200):
        
        playsound("facial/audio/front30down.mp3")
    k=cv2.waitKey(1)
    if(k%256==27):
        break
    if(counter==1400):
        break
    img_name="img_{}.png".format(counter)
    counter=counter+1
    cv2.imwrite('facial/database/user/'+img_name,frame)
cam.release()
cv2.destroyAllWindows()
playsound("facial/audio/message.mp3")
print("Photos captured")
sys.stdout.flush()
curr_path = os.getcwd()
curr_path=os.path.join(curr_path,"facial")

print("Loading face detection model")
proto_path = os.path.join(curr_path, 'model', 'deploy.prototxt')
model_path = os.path.join(curr_path, 'model', 'res10_300x300_ssd_iter_140000.caffemodel')
face_detector = cv2.dnn.readNetFromCaffe(prototxt=proto_path, caffeModel=model_path)

print("Loading face recognition model")
recognition_model = os.path.join(curr_path, 'model', 'openface_nn4.small2.v1.t7')
face_recognizer = cv2.dnn.readNetFromTorch(model=recognition_model)

data_base_path = os.path.join(curr_path, 'database')

filenames = []
for path, subdirs, files in os.walk(data_base_path):
    for name in files:
        filenames.append(os.path.join(path, name))

face_embeddings = []
face_names = []
count=0
for (i, filename) in enumerate(filenames):
    print("Processing image {}".format(filename))
    count=count+1
    image = cv2.imread(filename)
    image = imutils.resize(image, width=600)

    (h, w) = image.shape[:2]

    image_blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0), False, False)

    face_detector.setInput(image_blob)
    face_detections = face_detector.forward()

    i = np.argmax(face_detections[0, 0, :, 2])
    confidence = face_detections[0, 0, i, 2]

    if confidence >= 0.5:

        box = face_detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")

        face = image[startY:endY, startX:endX]

        face_blob = cv2.dnn.blobFromImage(face, 1.0/255, (96, 96), (0, 0), True, False)

        face_recognizer.setInput(face_blob)
        face_recognitions = face_recognizer.forward()

        name = filename.split(os.path.sep)[-2]

        face_embeddings.append(face_recognitions.flatten())
        face_names.append(name)

f = open("facial/unknownfacedata.pickle", "rb")
unknownfacedata=pickle.load(f)
f.close()
face_embeddings.extend(unknownfacedata["embeddings"])
face_names.extend(unknownfacedata["names"])
data = {"embeddings": face_embeddings, "names": face_names}
le = LabelEncoder()
labels = le.fit_transform((data["names"]))

recognizer = SVC(C=1.0, kernel="linear", probability=True)
recognizer.fit(data["embeddings"], labels)
print(count)
f = open('facial/recognizer.pickle', "wb")
f.write(pickle.dumps(recognizer))
f.close()

f = open("facial/le.pickle", "wb")
f.write(pickle.dumps(le))
f.close()