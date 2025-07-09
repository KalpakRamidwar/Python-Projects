import random

n=random.randint(1,100)
gusses=1
a=-1
while(a!=n):
    a=int(input("Guess the number in between 1 to 100 :"))
   
    if(a>n):
        print("Lower number please :")
        gusses+=1
    elif(a<n):
        print("Higher number please :")
        gusses+=1

print(f"You have guess the number {n} in {gusses} attempts ")