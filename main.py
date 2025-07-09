import random

# SNAKE, WATER, GUN GAME

'''
snake=s=1
water=w=-1
gun=g=0
'''

computer=random.choice([1,0,-1])
youstr=input("Enter your choice :")
youdict={"s":1,"w":-1,"g":0}
reversedict={1:"snake",-1:"water",0:"gun"}
you=youdict[youstr]
comp=reversedict[computer]

# print(f"You choose {reversedict[you]} \ncomputer choose {reversedict[comp]}")

if(computer==you):
    print("Game Draw !")
else:
    if(computer==1 and you==-1):
        print("You Lose !")
    elif(computer==1 and you==0):
        print("You Win !")
    elif(computer==-1 and you==0):
        print("You Lose !")
    elif(computer==-1 and you==1):
        print("You Win !")
    elif(computer==0 and you==1):
        print("You Lose !")
    elif(computer==0 and you==-1):
        print("You Win !")
    else:
        print("Something went wrong!")