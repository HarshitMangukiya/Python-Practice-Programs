d=dict.fromkeys("age","unknown")
print(d)

d=dict.fromkeys(range(4,9),"hello")
print(d)

print(d.get(5))
# d.clear()
# print(d)
d1=d.copy()
print(d1)
