# importing cv2- opencv library in python for face recognition
import cv2 
#haarcascade_frontalface_default.xml is the default face recognition file
trainedfacemodel=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

webcam=cv2.VideoCapture(0)
while True:
    #webcam.read() function reads two things one is webcam is working fine or not and other one is video
    workingcorrectly,video=webcam.read()
    #we need to change the video in greyscale image
    blackandwhite=cv2.cvtColor(video,cv2.COLOR_BGR2GRAY)
    face=trainedfacemodel.detectMultiScale(blackandwhite)
    #this code is used to show the face in rectangle 
    for(x,y,w,h) in face:
        cv2.rectangle(video,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow("camera",video)
    key=cv2.waitKey(1)
    if(key==27):#key==27 is for escape key
        break