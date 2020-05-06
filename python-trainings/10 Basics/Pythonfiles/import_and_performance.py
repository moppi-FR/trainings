# -*- coding: utf-8 -*-
"""
This module shows how to import modules from the Python libraries and self created libraries.
Additionally some magic functions to test code performance are included
@author: Felix
"""

###############################Time Library####################################
import time


i = 0
while i < 10:
    print(i)
    i = i + 1
    time.sleep(0.1)



#############################Numerical Python##################################
import numpy as np

array = np.arange(10)
ones = np.ones((100,100,100), dtype = 'uint8')


#############################Selfmade Libraries################################
import my_test.testing as my_test
var = my_test.variable



#############################Code Performance##################################
size = 100000
liste = []
%timeit for i in range(size):liste.append(i)

%timeit np.arange(size)