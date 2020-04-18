a=("a","b","c","d",1,2,3,4)
print(a)
print(a[::-1])

for i in a:
    print(i)

b=(1,)
print(b)
c="A","b","c"
print(type(c))

d=("df","Sdf","fdg","gh")
a1,a2,a3,a4=d
print(a2)

e=("cx","df","fg",["sd",1,2,3])
e[1].append("df")
print(e)