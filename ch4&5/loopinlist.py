a=["a","b","c","d"]

for i in a:
    print(i)

b=[[1,2,3],[4,5,6],[7,8,9]]
print(b)
for i in b:
    print(i)

for sub in b:
    for i in sub:
        print(i)
print(f"this is {b[1][2]}")

print(type(b))

print(type(sub))
