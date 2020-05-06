# -*- coding: utf-8 -*-
"""
@author: Felix
More info on inheritance:
https://www.programiz.com/python-programming/inheritance
This module contains information on how to create classes and how to 
incorporate them into a program.
"""

#########################Classes###############################################

#Basic Example
class Example:
    def __init__(self, parameter1, parameter2):
        self.Parameter1 = parameter1
        self.Parameter2 = parameter2
        
FirstClass = Example('one','two')  
    
FirstClass.Parameter1   #returns value of Parameter1
FirstClass.Parameter1 = 1   #changes value of Parameter1

#Inheritance
class Example2(Example):
    def __init__(self, param3, param4):
        Example.__init__(self,param3,param4)

NewFirstClass = Example2('three','four')

#Example with method
class Human:
    def __init__(self,name, food, drink, sleep):
        self.Name = name
        self.Food = food
        self.Drink = drink
        self.Sleep = sleep
    
    def showSleeptime(self, days):
        return self.Sleep*days
    
Max = Human(name = 'Max',
            food = 'Bread',
            drink = 'Water',
            sleep = 8)

sleeptime = Max.showSleeptime(days = 300)


###############################################################################
#################################Task##########################################
###############################################################################

'''
1. Create a Class named Chessfigure and add all necessary attributes to the class.
    a) Create Instances for at least three different Chessfigures.

'''