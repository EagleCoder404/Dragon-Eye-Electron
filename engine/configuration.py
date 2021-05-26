import os
import shutil
import sys

try:
         import numpy
except ImportError as e:
         os.system('pip install numpy')

         
try:
         import scipy
except ImportError as e:
         os.system('pip install scipy')

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
except ImportError as e:
         print("numpy")
         failed=1

         
try:
         import scipy
except ImportError as e:
         print('scipy')
         failed=1

try:
         import sklearn
except ImportError as e:
         print('sklearn')
         failed=1

try:
         import imutils
except ImportError as e:
         print('imutils')
         failed=1

try:
         import pickle
except ImportError as e:
         print('pickle-mixin')
         failed=1

try:
         import cv2
except ImportError as e:
         print('opencv-python')
         failed=1
if(failed==1):
         print("fail")
else:
         print("success")






if os.path.exists('c:\\dragon-eye'):
         shutil.rmtree('c:\\dragon-eye')
if not os.path.exists('c:\\dragon-eye'):
         os.makedirs('c:\\dragon-eye')
         os.makedirs('c:\\dragon-eye\PROCTORING LOGS')
         os.makedirs('c:\\dragon-eye\CONFIGURATION LOGS')
         
file=open("c:\\dragon-eye\CONFIGURATION LOGS\systemlogs.txt","a")
for ele in list1:
         file.write(ele)
         file.write('\n')
file.close()
sys.stdout.flush()


         



