number=[1,2,3,5,8]
print(min(number))
print(max(number))

def large(num):
    return max(num)-min(num)

print(large(number))