a=5 #global
def sco():
    x=6 #local
    global y
    y=10
    return y

print(sco())
print(y)
