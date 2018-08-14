# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 12:22:08 2018

@author: dwive
"""

print("Hello There")
print("*********This is Designated Entry Screen**************")
print("######################################################")
print("Enter the Name")      
myName = input()
#print(" Name Entered is " + myName )
#print("This will be authorized with correct Password")
#print("Enter Password")
Password_1 =input()
if myName and Password_1 == "Pankaj" and "Delta!@" :
    print("Hello Authorized Person" + myName)
#elif myName and Password_1 == "Tango" and "Mango":
    print("Hello Authorized Person" + myName )
else :
    print(" Non Authorized")
print("######################################################")
    