a=dict.fromkeys(['name','age','address'],',harshut')
a=dict.fromkeys({'a','d'},'man')
a=dict.fromkeys(('a','d'),'man')
a=dict.fromkeys("sdsddfkjdf",'man')

a=dict.fromkeys(range(1,15),'df')
print(a)
b={'name':'man','age':'ram'}
print(b['age']) 
print(b.get('name'))
if b.get('name'):
    print(b.get('name'))
else:
        print("not hello")