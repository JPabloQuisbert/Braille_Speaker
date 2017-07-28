# -*- coding: cp1252 -*-
import sys
import cv2
import numpy as np

mt = []
for i in range(3):
    mt.append([])
    for j in range(2):
        mt[i].append(0)
        
#abrir una imagen
imagen1=cv2.imread('letra3.jpg')
cv2.namedWindow('imagen cargada', cv2.WINDOW_AUTOSIZE)
cv2.imshow('imagen cargada',imagen1)

#convertir en escala de gris
gris=cv2.cvtColor(imagen1,cv2.COLOR_BGR2GRAY)

#Aplicar suavizado Gaussiano
gaussiana = cv2.GaussianBlur(gris, (5,5), 0)
cv2.imshow('gauss',gaussiana)

# Detectamos los bordes con Canny
canny = cv2.Canny(gaussiana, 50, 150)

cv2.imshow('canny',canny)
m,n=canny.shape

roi=canny[0:m/3,0:n/2]
#buscar contornos
_,contornos, hierarchy = cv2.findContours(roi.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# Mostramos el número de monedas por consola
if(len(contornos)==1):
    mt[0][0]=1

roi2=canny[m/3:2*m/3-10,0:n/2]
cv2.imshow('roi2',roi2)
#buscar contornos
_,contornos2, hierarchy = cv2.findContours(roi2.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# Mostramos el número de monedas por consola
if(len(contornos2)==1):
    mt[1][0]=1

roi3=canny[2*m/3:m,0:n/2]
#buscar contornos
_,contornos3, hierarchy = cv2.findContours(roi3.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# Mostramos el número de monedas por consola
if(len(contornos3)==1):
    mt[2][0]=1

#####
roi4=canny[0:m/3,n/2:n]
#buscar contornos
_,contornos4, hierarchy = cv2.findContours(roi4.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# Mostramos el número de monedas por consola
if(len(contornos4)==1):
    mt[0][1]=1

roi5=canny[m/3:2*m/3,n/2:n]
#buscar contornos
_,contornos5, hierarchy = cv2.findContours(roi5.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# Mostramos el número de monedas por consola
if(len(contornos5)==1):
    mt[1][1]=1

roi6=canny[2*m/3:m,0:n/2:n]
#buscar contornos
_,contornos6, hierarchy = cv2.findContours(roi6.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# Mostramos el número de monedas por consola
if(len(contornos6)==1):
    mt[2][1]=1
    
print mt

k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
