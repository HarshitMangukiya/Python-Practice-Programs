name=input("enter name")

total=0
i=0
while i<len(name):
    x=name.count(name[i])
    print(name[i]+" "+str(x))
    
    i=i+1
