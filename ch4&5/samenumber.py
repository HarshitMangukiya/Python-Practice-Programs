a=[1,2,3,4,5,6,7]
b=[3,4,5,6,3,2,2]
c=[]
def funn(a,b):
    for i in a:
        for j in b:
            if i==j:
                c.append(i)

funn(a,b)
print(a)
print(b)
print(c)
    