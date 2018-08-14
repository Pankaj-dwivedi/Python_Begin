# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 16:48:34 2018

@author: dwive
"""

print("Hello ")
print(" ***************************************")
print ( " Enter Your NAme" )
myName = input()
print ( " Hi Mr. " + myName)
print ( " You will be authorized with proper Password: Please enter your Password" )
myPass = input()
print ( "Entered Password is " + myPass)
if myName == "Raghav" and myPass == "Delta" :
    print ( "Sector_0 printed ")
elif myName == "Raghav Trehan" and myPass == "Delta_1" :
    print(" Sector_1 printed" )
elif myName == "Raghav Trehan" and myPass == "Delta@1234" :
    print (" Sector_2 completed" )
else :
    print( " Not OK" )
    
    



