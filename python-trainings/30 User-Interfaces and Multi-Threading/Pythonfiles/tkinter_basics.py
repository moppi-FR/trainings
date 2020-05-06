# -*- coding: utf-8 -*-
"""
@author: Felix
Basic Elements of the tkinter Package used to create User Interfaces
"""


########################### TKINTER BASIC UI ##################################
import tkinter as tk

#Setting size of window to 800x600
width,height = 800,600

#Creating an Instance of a Tkinter window
window = tk.Tk()


#Setting windowsize to width and height. (width, height, offset x, offset y)
window.geometry("%dx%d+0+0" % (width,height))

#Setting WIndow Backgroundcolor - Optional (defuault = gray)
window.configure(background='black')



#Start UI
window.mainloop()

###############################################################################


########################### TKINTER UI FROM FUNCTION ##########################
import tkinter as tk

#Setting size of window to 800x600
width,height = 800,600

def createUI(w, h):
    '''
    Function to create an empty tkinter UI
    '''
    #Creating an Instance of a Tkinter window
    window = tk.Tk()
    
    
    #Automatically adapt window size to screensize if given size is 0
    if w == 0 and h == 0:
        w, h = window.winfo_screenwidth(), window.winfo_screenheight()
    
    
    #Setting windowsize to width and height. (width, height, offset x, offset y)
    window.geometry("%dx%d+0+0" % (w, h))
    
    #Setting WIndow Backgroundcolor - Optional (defuault = gray)
    window.configure(background='black')
    
    return w,h,window


#Start UI
width,height,root = createUI(width,height)
root.mainloop()

###############################################################################


##################### Button, Text and Listbox Widgets ########################

width,height,root = createUI(width, height)


#Buttonfunctions
def examButton1():
    print("Button Clicked")
    
def examButton2():
    #The Button will now print out the text of a specific Text Widget
    print(testText.get("1.0",'end-1c'))
    
def examButton3():
    #The Button will now print out the text of a specific Text Widget
    liste.append(testText.get("1.0",'end-1c'))
    testListbox.insert(tk.END, testText.get("1.0",'end-1c'))
    
#Button Widget
testButton = tk.Button(root,   #Rootwindow of this Button Widget
                    text = "This Button", #Buttontext
                    font = "Verdana 14 bold", #Textstyle ( "Style Size Features")
                    command = examButton3) #Buttonfunction that is called onClick
testButton.place(x = width*.1, y = height*.1) #Positioning Button Widget



#Text Widget
testText = tk.Text(root, #Rootwindow of this Text Widget
                   font = "Verdana 22 bold", #Textstyle ( "Style Size Features")
                   height=1, #Height of Text Widget - Number of Elements
                   width=22) #Width of Text Widget - Number of Elements
testText.place(x = width*.1, y = height*.2) #Positioning Text Widget



#Listbox Widget
testListbox = tk.Listbox(root, #Rootwindow of this Listbox Widget
                font = "Verdana 22 bold", #Textstyle ( "Style Size Features")
               height=7, #Height of Text Widget - Number of Elements
               width=22) #Width of Text Widget - Number of Elements
testListbox.place(x = width*.1, y = height*.3) #Positioning Listbox Widget


liste = [1,2,3,4,5,6]
for text in liste:
    testListbox.insert(tk.END, text)
#Add element at the Index of the listbox - This case is at the end


#Start UI
root.mainloop()

###############################################################################

############################### WIDGET MANAGEMENT #############################

#List Containing all Widgets
widget_list = []

#Adding testListbox to list. Index = 0
widget_list.append(testListbox)


###############################################################################
#################################Task##########################################
###############################################################################
'''
1. Create a Class called "Material" in a first module called "master_data", that has at least 5 attributes.
The "Material" class should contain materials necessary for industrial assembly tasks.
Choose the attributes accordingly.

2. Create a second module called "creation_ui" that can be used to perform the following functions:
    a) Create a new Material or add it to a list
    b) View Materials
    c) Delete Materials
'''
    

