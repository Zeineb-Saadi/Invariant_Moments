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
def distance_euc(file_path): # to calculate the distance between the moment of the image and the others 
    
    distance=[]
    raw_data = list(collection.find({},projection=exclude_data)
    imageMoments = list(collection.find({'path':file_path}, projection=exclude_data))
    df =  pd.DataFrame(raw_data)
    df1= pd.DataFrame(imageMoments)#the dataframe of the image that you choose
    j=0
    for i in df['centrale_moment']:
        for j in df1['centrale_moment']:
            dist1 =sqrt(sum([(abs(float(a))-abs(float(b))) ** 2 for a, b in zip(j, i)]))
            distance[j].append(dist1)
            j=j+1
    j=0
    for i in df['hu_moments']:
        for j in df1['hu_moments']:
            dist2 =sqrt(sum([(abs(float(a))-abs(float(b))) ** 2 for a, b in zip(j, i)]))
            distance[j].append(dist2)
            j=j+1
    j=0
    for i in df['zernike_moment']:
        for j in df1['zernike_moment']:
            dist3 =sqrt(sum([(abs(float(a))-abs(float(b))) ** 2 for a, b in zip(j, i)]))
            distance[j].append(dist3)
            j=j+1
        

    return(distance)
