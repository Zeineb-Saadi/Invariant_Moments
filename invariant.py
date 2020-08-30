from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
def centrale(file_path): 
    matrice=np.zeros(7)
    im=cv2.imread(file_path)
    im_gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    ret,thresh=cv2.threshold(im_gray,127,255,0)
    m=cv2.moments(thresh)
    cv2.imshow('image',im)
    #normalized central moments
    matrice[0]=m["nu20"]
    matrice[1]=m["nu11"]
    matrice[2]=m["nu02"]
    matrice[3]=m["nu30"]
    matrice[4]=m["nu21"]
    matrice[5]=m["nu12"]
    matrice[6]=m["nu03"]
    for i in range(7):#log transform
        matrice[i]=-1*copysign(1.0,matrice[i])*log10(abs(matrice[i]))
    return(matrice)
def zernike_moments(file_path):# put the file path of the image as the input
    im=cv2.imread(file_path)
    im_gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    ret,thresh=cv2.threshold(im_gray,127,255,0)
    zernike=mh.features.zernike_moments(thresh,255)
    cv2.imshow('image',im)
    for i in range(25):#log transform
        zernike[i]=-1*copysign(1.0,zernike[i])*log10(abs(zernike[i]))
    return(zernike)
def hu_moments(file_path):
    im=cv2.imread(file_path)
    im_gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    ret, th = cv2.threshold(im_gray, 127, 255, cv2.THRESH_BINARY)
    M = cv2.moments(th, True)
    H = cv2.HuMoments(M)
    hu=[0.0]*7
    for i in range(7):
         hu[i]=-1*copysign(1.0,H[i])*log10(abs(H[i]))
    return(hu)
def openfn():
    filename = filedialog.askopenfilename(title='open')
    return filename