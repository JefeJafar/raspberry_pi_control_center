#Raspberry Pi terminal menu / control panel to control 
# using SSH connection
#Project by Red Alert Technologies, LLC
#9/28/2020 

#Version 1.0

import time

print ("Welcome to your Raspberry Pi, Jafar!")
print ("Select command: ")
print ("---------------------------------")
print("A. Hello this is just the beta")
print("B. This is Option 2")
print("----------------------------------")
selection = input("Enter number: " )

if selection == "A":
    print("You chose option A, Thats it for now, be back for more ASAP!")
elif selection =="B":
    print ("You chose option B!")

else: 
    print ("Invalid Input")