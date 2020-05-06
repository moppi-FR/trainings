# -*- coding: utf-8 -*-
"""
@author: Felix
Module that contains examples for using multiple threads in a module
"""

#############################EXAMPLE SINGLE THREAD#############################

#Importing libraries
import time

print("main Thread started")


def my_function(name, sleeptime):
    print("Job: ", name, " started")
    
    for i in range(10):
        print(i)
        time.sleep(sleeptime)
    
    print("Job: ", name, " stopped")




#Starting Thread parallel to main-Thread
my_function('Counting', 0.5)

print("main Thread stopped")


###############################################################################


#############################EXAMPLE MULTITHREADING############################


#Importing libraries
import threading
import time

print("main Thread started")


def my_function(name, sleeptime):
    print("Thread: ", name, " started")
    
    for i in range(10):
        print(i)
        time.sleep(sleeptime)
    
    print("Thread: ", name, " stopped")




#Starting Thread parallel to main-Thread
my_thread = threading.Thread(target = my_function, args=('Counting', 0.5))
my_thread.start()

print("main Thread stopped")

###############################################################################

#######################SENSOR READOUT EXAMPLE##################################




#######################USING FUNCTIONS##########################
#importing libraries
import random
import time
import threading


#Checking the roomtemperature
def checkTemperature(room, temp_max, timer):
    #Creating a random Temperature
    temp = random.randint(15,35)
    while temp < temp_max:
        temp = random.randint(15,35)
        print("Current Temperature in ", room, " is: ",temp, "°C")
        time.sleep(timer)
    return temp


def my_function(name, maxTemp, freq):
    
    temp = checkTemperature(name, maxTemp, freq)   
    print("Temperature too high at ", temp, '°C')


my_thread = threading.Thread(target = my_function, args=('Livingroom', 34, 0.3))
my_thread.start()

####################USING CLASSES###############################
import threading
import time
import random


class Thermostat (threading.Thread):
    #Initializing Class
   def __init__(self, threadID, threadName, maxTemp, freq):
       #Initializing Parent Class (threading.Thread)
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.Name = threadName
      self.MaxTemp = maxTemp
      self.Freq = freq
      
    #The run Function contains the code executed in the Thread
   def run(self):
      print( "Starting " + self.Name)
      exitVal = self.checkTemperature(self.Name, self.MaxTemp, self.Freq)
      print("Too hot at: ", exitVal, "°C")
      print( "Exiting " + self.Name)
      
    #Checking the roomtemperature
   def checkTemperature(self, room, temp_max, timer):
        #Creating a random Temperature (simulating a sensor)
        temp = random.randint(15,35)
        while temp < temp_max:
            temp = random.randint(15,35)
            print("Current Temperature in ", room, " is: ",temp, "°C")
            time.sleep(timer)
        return temp



# Create a new thread
LivingRoom = Thermostat(1, "Livingroom", 34, 0.2)

# Start new Thread
LivingRoom.start()


###############################################################################
#################################Task##########################################
###############################################################################
'''
1. Create a Thread that displays your current CPU and RAM usage.
Stop/Kill the thread if certain conditions are met.
'''
