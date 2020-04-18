# win=50
import random

win=random.randint(10,)
print(win)
num=int(input("enter the number"))
i=0
game=False

while not game:
    if num==win:
        print("you win number"+str(num))
        game=True
    if num<win:
        print("low")
        i=i+1
        num=int(input("enter again"))   
    else:
        print("high")
        i=i+1
        num=int(input("enter again"))
            