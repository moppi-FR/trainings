# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 17:15:51 2020

@author: RIEDEFE
Module that contains Code examples for different Client-Server-Communication methods
"""

#Import Numpy library as np --> it is best practice to import the library this way
import numpy as np

#################### Creating example arrays ##################################

# 1-D Array with evenly spaced values
one_d = np.array([1,2,3,4,5,6])
arange = np.arange(0,100, 5)
# 2-D Arrays
two_d = np.array([[1,2,3],[4,5,6]])
zeros = np.zeros((100,100))
ones = np.ones((100,100))
eye = np.eye(100)
#3-D Arrays
three_d =np.array([[[100,100,100],[100,100,100]]])
ones_3d = np.ones((10,10,3))

#Setting Datatype
float_array = np.zeros((10,10,4), dtype = np.float64)

#Saving Arrays
np.save('myArray.npy', ones)
#Loading Arrays
my_loaded_array = np.load('myArray.npy')


##################### Working with Arrays #####################################

'''Visualising an array'''

#For Visualisation of arrays, the library matplotlib can be used
import matplotlib.pyplot as plt

#creating a scatterplot of a one-dimensional array
plt.scatter(np.arange(0,len(arange)), arange)
#plot a line
plt.plot(np.arange(0,len(arange)), arange)
#plot both in a single window
plt.subplot(121), plt.scatter(np.arange(0,len(arange)), arange)
plt.subplot(122), plt.plot(np.arange(0,len(arange)), arange)

#plotting a two-dimensional array
#as an 'image'
plt.imshow(eye, cmap = 'gray')



'''Arithmetics'''

#Adding a value to every item in an array
#Works equally for +-*/
threes = ones + 2

#Adding the values of two array together
#ATTENTION! --> Arrays must have same dimensions and datatypes
#Works equally for +-*/
new_zeros = eye * zeros


'''Matrix Multiplication'''
matrix = np.array([[10,20,30],[5,7,3]])
#Transposing a matrix
transpose = matrix.T
#Multiplication
result1 = np.dot(matrix,transpose)
result2 = np.dot(transpose,matrix)



'''Combining and Changing Shapes of Arrays'''

#Arrays can be stacked along their dimensions, thereby adding rows, columns or any other dimension
#stacking arrays along the horizontal axis --> adding lines
stack_lines = np.concatenate((zeros,ones), axis = 0)

#stacking arrays along the vertical axis --> adding columns
stack_columns = np.concatenate((zeros,ones), axis = 1)

#stacking arrays along the depth axis --> adding layers
stack_layer = np.concatenate((float_array,ones_3d), axis = 2)


#Reshaping Arrays
arange = np.reshape(arange, (4,5))

#Adding a dimension
arange = np.reshape(arange, (arange.shape[0], arange.shape[1], 1))


'''Changing specific values of an array'''
#creating an array of random values between 0 and 1
random_array = np.random.rand(100,100)
plt.imshow(random_array, cmap = 'gray')
#Selecting a specific area
area = random_array[10:50, 20:30]
plt.imshow(area, cmap = 'gray')

#Creating a mask for a certain condition
#A mask is an array of boolean values that contains information whether or not an item fulfills a certain condition
mask = area < .5
plt.imshow(mask, cmap = 'gray')

#applying a mask to an array -> ARRAY and MASK have to be of the SAME dimensions
area[mask] *= 0
#As can be seen in the plots, the operation is only executed for the items that are "True" in the mask
plt.subplot(121), plt.imshow(mask, cmap = 'gray')
plt.subplot(122), plt.imshow(area, cmap = 'gray')
