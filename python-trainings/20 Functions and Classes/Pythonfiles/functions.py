# -*- coding: utf-8 -*-
"""
@author: Felix
This module contains information on how to create functions and how to 
incorporate them into a program.
"""

#########################Functions#############################################
import math

math.sin(90)

#Minimal Content
def add():      #defining a function
    a = 3 + 2
    print(a)

add()           #calling a function

#Including parameters
a,b = 4,1
def sub(sub1,sub2):
    print(sub1-sub2)

sub(a,b)

#Getting a return value
def mul(fac1,fac2):
    return fac1*fac2

c = mul(a,b)

#Changing a global variable within a function
def div(div1, div2):
    global c
    c *= div1
    return c/div2

d = div(a,b)    #When not using parameter names
e = div(div2 = a, div1 = b)     #When  using parameter names

###############################################################################

###########################Help################################################

#Existing help example
math.floor()    #Move cursor between brackets and press Ctrl+I

#Creating help instructions for sel-written functions or classes
def test(first_variable, second_variable):
    """This is the description for the function.
    \n <-'backslash + n' is used as a linebreak.
    \n----------------------Parameters----------------------
    \n first_variable   = usage, range, datatype etc.
    \n second_variable  = usage, range, datatype etc."""
    return 3


test()

###############################################################################

#####################Variable & Function Names#################################

#camelCase
doSomething = 1

#Underscore
do_something = 1


###############################################################################
#################################Task##########################################
###############################################################################

'''
1. Create a module with the following functions:
    add -> Add
    sub -> Subtract
    mul -> Multiply
    div -> Divide
    mod -> Modulus
2. Create a second module in which you import the module created in 1 and
    a) create two variable of datatype int
    b) perform all the fucntions of the module from 1 with these variables
    c) create a function that performs an adjustable number of the created
    mathematical operations on variables, depending on the variable's current
    value. -> This is your first self-written ALGORITHM
'''