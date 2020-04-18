a=[1,2,3,4,5,6,6,4,3,3,4,5]

b=[i*i if i%2==0 else -i for i in a]

print(b)