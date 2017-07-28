# -*- coding: cp1252 -*-
import os
import cv2
import numpy as np
import time

roi = np.zeros((300,512,3), np.uint8)
roi2 = np.zeros((300,512,3), np.uint8)
roi3 = np.zeros((300,512,3), np.uint8)
roi4 = np.zeros((300,512,3), np.uint8)

cap = cv2.VideoCapture(0)
cv2.namedWindow('image')
def nothing(x):
    pass
a=1

while(1):
    # Tomar cada frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_mask = np.array([29,136,179])
    upper_mask = np.array([42,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_mask, upper_mask)

    #Filtrar el ruido con un CLOSE/OPEN
    kernel = np.ones((6,6),np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    #converit a escala gris
    gris=cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
    # Aplicar suavizado Gaussiano
    gaussiana = cv2.GaussianBlur(gris, (5,5), 0)
    cv2.imshow('GAUSS',gaussiana)

    # Detectamos los bordes con Canny
    canny = cv2.Canny(gaussiana, 50, 150)
    cv2.imshow('canny',canny)

    #momentos
    moments = cv2.moments(mask)
    area = moments['m00']

    #buscar contornos
    _,contornos, hierarchy = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    #cv2.drawContours(frame,contornos,-1,(0,0,255), 2)

    areas = [cv2.contourArea(c) for c in contornos]

    i = 0
    for extension in areas:
        if extension > 50000:
            actual = contornos[i]
            #Aproximar el numero de vertices
            approx = cv2.approxPolyDP(actual,0.1*cv2.arcLength(actual,True),True)
            if len(approx)==4:

                cnt=contornos[0]
                xr,yr,wr,hr = cv2.boundingRect(cnt)
                #cv2.rectangle(frame,(xr,yr),(xr+wr,yr+hr),(255,0,0),2)

                #rectangulo rotado
                rect = cv2.minAreaRect(cnt)
                box = cv2.boxPoints(rect)
                
                box = np.int0(box)
                #cv2.drawContours(frame,[box],0,(0,0,255),2)                

                #dibujar linea
                
                #cv2.line(frame,(xr,yr+hr/3),(xr+wr,yr+hr/3),(0,200,200),2)
                #cv2.line(frame,(xr,yr+2*hr/3),(xr+wr,yr+2*hr/3),(0,200,200),2)

                #cv2.line(frame,(xr+wr/2,yr),(xr+wr/2,yr+hr),(0,200,200),2)
                #cv2.line(frame,(box[0][0],box[0][1]),(box[2][0],box[2][1]),(0,200,200),2)

                #recortar area 1
                
                roi=frame[yr:yr+hr-5,xr:xr+wr]
                
                cv2.imwrite('save_2.jpg', roi)
                cv2.imshow('roi', roi)

                
                '''

                roi=frame[yr:yr+hr-5,xr:xr+wr/4]
                cv2.imshow('roi1', roi)
                roi2=frame[yr+5:yr+hr-5,xr+wr/4:xr+wr/2]
                cv2.imshow('roi2', roi2)

                roi3=frame[yr+5:yr+hr-5,xr+wr/2:xr+3*wr/4]
                cv2.imshow('roi3', roi3)
                roi4=frame[yr+5:yr+hr-5,xr+5+3*wr/4:xr+wr-5]
                cv2.imshow('roi4', roi4)
                '''

              

                
            i = i+1
            
    gris_roi=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    gauss_roi = cv2.GaussianBlur(gris_roi, (5,5), 0)
    canny_roi = cv2.Canny(gauss_roi, 50, 150)
    cv2.imshow('canny1', canny_roi)
    
    #buscar contornos
    _,cont_roi,_ = cv2.findContours(canny_roi.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    # Mostramos el número de puntos 1
    print("He encontrado {} puntos 1".format(len(cont_roi)))

    gris_roi2=cv2.cvtColor(roi2,cv2.COLOR_BGR2GRAY)
    gauss_roi2 = cv2.GaussianBlur(gris_roi2, (5,5), 0)
    canny_roi2 = cv2.Canny(gauss_roi2, 50, 150)
    cv2.imshow('canny2', canny_roi2)
    
    #buscar contornos
    _,cont_roi2,_ = cv2.findContours(canny_roi2.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    # Mostramos el número de puntos 2
    print("He encontrado {} puntos 2".format(len(cont_roi2)))

    gris_roi3=cv2.cvtColor(roi3,cv2.COLOR_BGR2GRAY)
    gauss_roi3 = cv2.GaussianBlur(gris_roi3, (5,5), 0)
    canny_roi3 = cv2.Canny(gauss_roi3, 50, 150)
    cv2.imshow('canny3', canny_roi3)
    
    #buscar contornos
    _,cont_roi3,_ = cv2.findContours(canny_roi3.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    # Mostramos el número de puntos 3
    print("He encontrado {} puntos 3".format(len(cont_roi3)))
    
    gris_roi4=cv2.cvtColor(roi4,cv2.COLOR_BGR2GRAY)
    gauss_roi4 = cv2.GaussianBlur(gris_roi4, (5,5), 0)
    canny_roi4 = cv2.Canny(gauss_roi4, 50, 150)
    cv2.imshow('canny4', canny_roi4)
    
    #buscar contornos
    _,cont_roi4,_ = cv2.findContours(canny_roi4.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    # Mostramos el número de puntos 4
    print("He encontrado {} puntos 4".format(len(cont_roi4)))
    


    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

for i in range(3):
    print i
    time.sleep(2)


cap.release()

os.system('start vision_palabra.py')

cv2.destroyAllWindows()

