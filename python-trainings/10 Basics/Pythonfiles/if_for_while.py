# -*- coding: utf-8 -*-
"""
@author: Felix
If-Statements along with for and while loops build the basis of most programs.
This module contains examples for them.
"""
a,b,c = 1,2,3
################################If Statement###################################

#Comparing two variables for one condition
if a == b:
    print("a = b")
else:
    print("a != b")
    
#Comparing two variables for multiple conditions
if a == b:
    print("a = b")
elif a < b:
    print("a < b")
else:
    print("a > b")
    
#Comparing multiple variables for one condition
if a < c and b < c:
    print("c is largest")
else:
    pass

#Multi-Levelled Conditions
if a == 1:
    if not b == a:
        print("Works")
        
###############################################################################

##########################For Loops############################################
        
liste = [1,2,3,4,5,6,7,8]
len(liste)  #Length of the list-Object

#Iterate over values of a list-Object
for i in range(len(liste)):
    print(liste[i])

#Change every value of a list    
for i in range(len(liste)):
    liste[i] = liste[i] + 5
    
#Add values to a list using a for loop
liste2 = []
for i in range(10):
    liste2.append(i)

#Iterate over elements of a list    
liste3 = [[1,2],[3,4],[5,6],[7,8]]
for item in liste3:
    print(item)
    
#Multilevelled iteration   
liste3 = [[1,2],[3,4],[5,6],[7,8]]
for item in liste3:
    for value in item:
        print(value)
    
#Stop looking through a list, if a certain item is found
for item in liste:
    if item == 4:
        break
    else:
        print(item)
        
#Skipping an iteration, if a certain item is found
for item in liste:
    if item == 4:
        continue
    else:
        print(item)
        
###############################################################################
#%%
########################While Loops############################################

#Endless loop
while True:
    print("Hello")

#Loop n times
i = 0
while i < 10:
    print(i)
    i = i + 1


#%%
###############################################################################
#################################Task##########################################
###############################################################################
'''
1. Recreate the functionalities of the for loops, using while loops
2. Create a list object with 20 elements.
    a. Create a for loop that iterates over the object from the second until
       the second to last element and "print" every element to the console.
    b. Now let the for loop only print every second element.

'''
    
    
    
    
    