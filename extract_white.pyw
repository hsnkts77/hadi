import cv2
import numpy as np

def extract_white(img,resize=True):
    if resize == True:
        img = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([0,0,0])
    upper = np.array([255,12,255])
    mask = cv2.inRange(hsv,lower,upper)
    res  = cv2.bitwise_and(img,img,mask=mask)
    #res = cv2.GaussianBlur(res,(3,3),0)
    return res
