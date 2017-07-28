# -*- coding: cp1252 -*-
import os
import cv2
import numpy as np
#ajuste de altura
s1,s2=15,80
        
#abrir una imagen
imagen1=cv2.imread('save_2.jpg')
cv2.namedWindow('imagen cargada', cv2.WINDOW_AUTOSIZE)
cv2.imshow('imagen cargada',imagen1)

#convertir en escala de gris
#gris=cv2.cvtColor(imagen1,cv2.COLOR_BGR2GRAY)

# Aplicar suavizado Gaussiano
#gaussiana = cv2.GaussianBlur(gris, (5,5), 0)
#cv2.imshow('imagen cargada 3',gaussiana)

# Detectamos los bordes con Canny
#canny = cv2.Canny(gaussiana, 50, 150)
#cv2.imshow('canny',canny)



m,n,_=imagen1.shape

roi=imagen1[s1:m-s2,0:n/4]
#buscar contornos
#_,contornos, hierarchy = cv2.findContours(roi.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# Mostramos el número de monedas por consola
cv2.imshow('roi1',roi)
cv2.imwrite('letra1.jpg', roi)

roi2=imagen1[s1:m-s2,n/4:n/2]
#buscar contornos
#_,contornos2, hierarchy = cv2.findContours(roi2.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# Mostramos el número de monedas por consola
cv2.imshow('roi2',roi2)
cv2.imwrite('letra2.jpg', roi2)

roi3=imagen1[s1:m-s2,n/2:3*n/4]
#buscar contornos
#_,contornos3, hierarchy = cv2.findContours(roi3.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# Mostramos el número de monedas por consola
cv2.imshow('roi3',roi3)
cv2.imwrite('letra3.jpg', roi3)

#####
roi4=imagen1[s1:m-s2,3*n/4:n]
#buscar contornos
#_,contornos4, hierarchy = cv2.findContours(roi4.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# Mostramos el número de monedas por consola
cv2.imshow('roi4',roi4)
cv2.imwrite('letra4.jpg', roi4)


os.system('start vision_foto.py')

k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
