a=10
b=int(input("enter your guess number"))

if b==a:
    print("you win")
else:
        print("you not win")
        if b<a:
            print("low")
        else:
            print("high")    