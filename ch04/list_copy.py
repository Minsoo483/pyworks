a=[1,2,3,4,5,6]
a2=[]

for i in a:
    a2.append(i)
print("a2 =",a2)

a3=[]
for i in a:
    if i % 2 != 0:
        a3.append(i)
print("a3 =",a3)
