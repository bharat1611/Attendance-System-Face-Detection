import cv2
import face_recognition
import pickle
import os

#importing the mode images into a list
folderPath = 'Images'
pathList = os.listdir(folderPath)
imgList = []
studentIds = []
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    #with .png
    print(path)
    #removing .png
    print(os.path.splitext(path)[0])
print(len(imgList))
