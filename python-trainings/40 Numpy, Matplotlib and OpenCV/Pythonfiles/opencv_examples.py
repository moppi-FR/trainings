# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 08:29:35 2020

@author: RIEDEFE
"""
#Importing Library
import cv2
import matplotlib.pyplot as plt
import numpy as np

#loading image
img = cv2.imread('mark_0.jpg')

#Visualising Image
cv2.imshow('Image', img)
plt.imshow(img)

#Converting Image Colorspaces
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img2)



'''Finding edges and contours'''
#Edges using Canny Edge Detection
edges = cv2.Canny(img2, 0, 150)
plt.imshow(edges, cmap = 'gray')

#Contours
#Create Grayscale Image
img_grayscale = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)
#Thresholding image
ret,thresh1 = cv2.threshold(img_grayscale,80,255,cv2.THRESH_BINARY)
plt.imshow(thresh1, cmap = 'gray')
#Getting Contours of only the outer layer
contours, hierarchy = cv2.findContours(thresh1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
#Getting contours of multiple layers
contours, hierarchy = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)


contour_img = np.copy(img2)
for contour in contours:
    contour_img = cv2.drawContours(contour_img, [contour], -1, (255), 1)
    
plt.imshow(contour_img)





#saving an image
cv2.imwrite('myImageName.jpg', contour_img)
