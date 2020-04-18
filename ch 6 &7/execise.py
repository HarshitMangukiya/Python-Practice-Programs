
def fun(x):
    y={}
    for i in range(0,x):
        print(i)
        z=i*i*i 
        y[i]=z
    print(y)

a=int(input("enter the number"))
fun(a)
