a=[1,2,3,[4,5,6],[2,4,4]]

def funn(a):
    y=1
    for i in a:
       x=type(i)
       if x==list:
           y=y+1
           return y

print(f"this number of list avliable {funn(a)}")