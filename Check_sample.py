# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 19:00:10 2018

@author: dwive
"""

print("Enter your name")
myName = input()
print ("Please enter your Password  Mr. " +  myName)
Password_1= str(input())
if myName and Password_1 == "Pankaj" and "Delta@1234":
      print("Hello Mr. Pankaj Yor are authorized" )
else :
    print (" You are not authorized Mr. ")