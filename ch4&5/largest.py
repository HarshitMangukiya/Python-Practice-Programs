a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))

 
def larg(a,b,c):
    if a>b and a>c:
        print("this is the big"+str(a))
    elif b>c:
        print("this is the big"+str(b))
    else:
        print("this is the big"+str(c))
        

larg(a,b,c)