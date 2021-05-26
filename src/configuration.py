import os
import shutil
import sys
list1=[]
try:
         import numpy
except ImportError as e:
         os.system('pip install numpy')

         
try:
         import scipy
except ImportError as e:
         os.system('pip install scipy')

try:
         import playsound
except ImportError as e:
         os.system('pip install playsound')
         
try:
         import sklearn
except ImportError as e:
         os.system('pip install sklearn')
         

try:
         import imutils
except ImportError as e:
         os.system('pip install imutils')


try:
         import pickle
except ImportError as e:
         os.system('pip install pickle-mixin')

try:
         import cv2
except ImportError as e:
         os.system('pip install opencv-python')

'''Checking if all the packages are successfully present in the system'''
failed=0
try:
         import numpy
         list1.append("numpy is working")
except ImportError as e:
         print("numpy")
         failed=1
try:
         import playsound
         list1.append("playsound is working")
except ImportError as e:
         print("playsound")
         failed=1
         
try:
         import scipy
         list1.append("scipy is working")
except ImportError as e:
         print('scipy')
         failed=1

try:
         import sklearn
         list1.append("sklearn is working")
except ImportError as e:
         print('sklearn')
         failed=1

try:
         import imutils
         list1.append("imutils is working")
except ImportError as e:
         print('imutils')
         failed=1

try:
         import pickle
         list1.append("numpy is working")
except ImportError as e:
         print('pickle-mixin')
         failed=1

try:
         import cv2
         list1.append("cv2 is working")
except ImportError as e:
         print('opencv-python')
         failed=1
if(failed==1):
         print("fail")
else:
         print("success")





'''
if os.path.exists('c:\\dragon-eye'):
         shutil.rmtree('c:\\dragon-eye')
if not os.path.exists('c:\\dragon-eye'):
         os.makedirs('c:\\dragon-eye')
         os.makedirs('c:\\dragon-eye\PROCTORING LOGS')
         os.makedirs('c:\\dragon-eye\CONFIGURATION LOGS')
         os.makedirs('c:\\dragon-eye\PROCTORING LOGS\database')
         
file=open("c:\\dragon-eye\CONFIGURATION LOGS\systemlogs.txt","a")
for ele in list1:
         file.write(ele)
         file.write('\n')
file.close()
'''
sys.stdout.flush()


         



