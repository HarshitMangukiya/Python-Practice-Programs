a={1,2,3,4,65,2,3,'a','b'}
print(a)

if "a" in a:
    print("avilable")
else:
    print("not ")

for i in a:
    print(i)

b={1,2,3,4}
c={3,4,5,6,6}

union=b|c
print(union)

intersect=b&c
print(intersect)