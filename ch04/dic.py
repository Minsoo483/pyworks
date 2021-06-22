person = {}

print(person)

person['name'] = 'Lim'
person['age'] = 26

print(person)

person['address'] = 'Incheon'
print(person)


for key in person:
    print(person[key])
    
del person['address']
#dic.pop('address')

print(person)
