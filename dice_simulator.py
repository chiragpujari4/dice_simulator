# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 20:45:01 2024

@author: Chirag Pujari
"""

#Jay Shree Ganeshaya Namah
#Jay Mata Di

import random

print("Welcome to the Dice Simulator: ")
print("We have three types of dices which are as follows: ")
print("1.) Dice 1 : It is a normal dice.")
print("2.) Dice 2 : It is a dice which have high chances of getting the number 4.")
print("3.) Dice 3 : It is a dice which have high chances of getting the number 6.")

dice_select=int(input("Enter the respective number of Dice which you want: "))

if(dice_select==1):
    while True:
        inp=input("To roll the dice press <Enter>: ")
        dice_random=random.randint(1, 6)
        print("You got: ", dice_random)

if(dice_select==2):
    while True:
        inp=input("To roll the dice press <Enter>: ")
        li4=[1,2,3,4,4,4,4,5,6]
        dice_random=random.choice(li4) 
        print("You got: ", dice_random)
        
if(dice_select==3):
    while True:
        inp=input("To roll the dice press <Enter>: ")
        li6=[1,2,3,4,5,6,6,6,6,6,6]
        dice_random=random.choice(li6) 
        print("You got: ", dice_random)        
        
else:
    exit()      
    
    
    
    
    
    