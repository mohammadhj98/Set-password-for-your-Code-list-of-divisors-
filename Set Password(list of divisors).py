#Set password for your Code
#if user enter a correct password can enter to your Code

import os
import time

counter = 0

while True:
    counter +=1
    if counter == 4:
        break
    password = input("enter a password = ")

    j = 1
    while j <=5:
        print(".",end="")
        j +=1
        time.sleep(0.5)

    if password == "12345":
        os.system("cls")
        break
        os.system("cls")
        print("Error! , invalidpassword! ")
if counter !=4:
    number = int(input("enter a number : "))
    i = 1

    while i <= number :
        if number % i == 0:
            print(i,end="\t")
        i += 1
    
