def fibona(num):
    x=0
    y=1
    if num==0:
       print(x)
    elif num==1:
        print(y)
    
    for i in range(num-2):
        c=x+y
        x=y
        y=c
        print(y)
        
    
 

num=int(input("enter the number"))
fibona(num)