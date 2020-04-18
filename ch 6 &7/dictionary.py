user={"name":"harshit","age":34}
print(user)
usr2=dict(name="harshit",age=34)
print(usr2)
print(usr2["name"])

d={
    "name":"harshit",
    "age":23,
}
print(d["name"])
print(type(d))

user=dict(name="harshit",age=84,address="archan soc")
print(user["address"])
print(user)

h={}
h["name"]="harshit"
h["age"]=34 
print(h)

if 34 in h.values():
    print("hello")
else:
    print("error")

#key
for i in h:
    print(i)

#values
for i in h.values():
    print(i)

usr=h.items()
print(usr)
print(type(usr))