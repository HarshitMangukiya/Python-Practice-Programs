a=[1,2,3,4,5,2,32,2,23,3,3,2,]
print(a)
print(list(set(a)))
b={1,2,3,4,2,3}
print(b)
b.add(9)
# b.remove(2)
print(b)
# b.discard(3)
print(b)
# b.clear()
print(b)

print("this is copy")

c=b.copy()
print(c)