a=[1,32,4,4,5,5,6]
a.append("hello")
a.insert(2,"harshit")
print(a)
b=["a","b","c","d","e"]
marge=a+b
print(marge)

a.extend(b)
a.append(b)
print(a)
print(b)