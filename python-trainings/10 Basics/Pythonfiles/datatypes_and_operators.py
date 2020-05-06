# -*- coding: utf-8 -*-
"""
@author: Felix
This module contains some of the most commonly used datatypes and operators in python,
along with examples and descriptions.
"""

######################Common Datatypes#########################################

=   #assign a value

a = 1    #int
b = 2.99999   #float
c = 'Hello World'   #String
d = "Hello World"   #String
e = True    #Boolean
f = False   #Boolean
g = [1,2,3]     #List 1D
h = [[1,2,3],[4,5,6]]   #List 2D
i = [[[1,2],[3,4]],[[5,6],[7,8]]]   #List 3D
j = (1,2,3)     #Tuple
k = b'hello'    #Byte
l = {"First":12,"Second":456,"Third":789}   #Dictionary
m = ["Hallo",1,1.24]

#Accessing Liste, Tuples and Dictionaries
#Lists
g[0]        #Listvalue at index[row] = 0
h[0][1]      #Listvalue at index[row][column] = 0,1
i[1][1][1]    #Listvalue at index[row][column][level] = 1,1,1

#How to change datatypes of variables

a = str(a) #change int to String
c = int(c) #Change String to int. Does not work if String ist not in int format
c = int('1234') #Change String to int
b = int(b) #Change float to int -> Rundet immer ab
g = tuple(g) #Change List to Tuple
j = list(j) #Change Tuple to List

###############################################################################

##########################Operators############################################

#Comparison Operators

<   #smaller than
<=  #smaller than or equal to
>   #larger than
>=  #larger than or equal to
==  #equal to
1 < 2   #Answer is always a boolean



#Arithmetic Operators

#Basic
1+2
1-2
1/2
1*2

#Modulus : remainder of a division
11%2    #Answer is 1

#Exponent
4**2



#Logical Operators

and #is true if chained conditions are all true
or  #is true if at least one of the chained conditions is true
not #is true if the condition is false

1 < 2 and 2 < 3
1 < 2 or 3 < 2
not 1 < 0


###############################################################################
#################################Task##########################################
###############################################################################

'''
1. Create a multidimensional Dicitonary
2. Research the following operators and their uses
    +=
    *=
    //=
    !=
'''




