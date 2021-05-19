# Importing necessary libraries 

from easygui import *
import easygui as gui

import numpy as np
import sys
from get_recommendation import get_recommendations

# maxing out numpy arrray display size for easygui display 
#np.set_printoptions(threshold=sys.maxsize)


def field_check(msg, title, fieldNames):
    '''
    This function checks for missing user input values in the multienterbox
    and returns the user input as fieldValues variable
    
    Parameters:
    
    msg, title and fieldnames of the multi-enterbox GUI
    
    '''
    
    fieldValues = multenterbox(msg, title, fieldNames)
    
    # Loop with conditionals to make sure that none of the user input 
    # fields are left blank
    while 1:
        if fieldValues is None: break
        errmsg = ""
        for i in range(len(fieldNames)):
            if fieldValues[i].strip() == "":
                errmsg += ('Movie is a required field.\n\n')
        if errmsg == "":
            break # if no empty fields found, proceed with next codeblock
        # Saving user input as list in fieldValues variable
        fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
    
    
    
    return fieldValues


def tag_entry():
    ''' 
    This function defines the easygui multenterbox parameters and calls
    on the field_check functions, if field/user input is retrieved function
    calls on similarity test and if a match is not found user gets returned 
    to the same window  
    '''
    
    # defining easygui multenterbox parameters
    msg = "Enter movie, we will get you similar"
    title = 'Search '                        
    fieldNames = ["Tag"]
    
    # calling on field_check() to check for missing user input and to
    # save user input as fieldValues variable
    fieldValues = field_check(msg, title, fieldNames)
    
    # If user input is not empty, slice list element and save in variable
    if fieldValues != None:
        global user_input
        user_input = fieldValues[0]
        
        # here we call on a function which basically tests for string
        # similarity. if user press cancel, user gets returned to main menu 
        similarity_test(user_input)
    else:
        tag_entry()



def similarity_test(user_input):
    '''
    This function will call get recommendation
    '''
    
    
    result = (get_recommendations(user_input))

    result = result.to_string()
    gui.textbox(msg='Movies recommended are ', text=(result),title='Movies')
    
    
     
# this is start point of app
if __name__ == '__main__':
    tag_entry()