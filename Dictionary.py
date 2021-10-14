from typing import Collection


# Dictionary ----> descriptive data Collection
# does not store the value by index

person = {
    'firstName' : "Kiran",
    'lastName' : "Dudhane",
    'age' : 25
}

print(person['firstName'])    # to fatch value
print(person['age'])

person['firstName'] = "Suraj"   # to update value
print(person)


person['Skills'] = "Javascript","Python"   # to update the dictionary
print(person)


for item in person:                          # for loop on dictionary
    print(item,person[item])


for item in person.keys():
    print(item)

for item in person.values():
    print(item)

for x,y in person.items():
    print(x,y)


print('------------------------------------------------>')


Students = [{
    'firstName' : "Kiran",
    'lastName' : "Dudhane",
    'age' : 25,
    'rollNo' : 125
},
{
    'firstName' : "suraj",
    'lastName' : "Dudhane",
    'age' : 20,
    'rollNo' : 145
},
{
    'firstName' : "Tejal",
    'lastName' : "Dudhane",
    'age' : 16,
    'rollNo' : 198
},
{
    'firstName' : "Tushar",
    'lastName' : "Dudhane",
    'age' : 31,
    'rollNo' : 98
}
]

# print(Students[0]['firstName'])
# print(Students[1]['age'])
# print(Students[2]['rollNo'])

for key in Students:
    for x,y in key.items():     # using for loop to print all key and values in array with object elements
        print(x,y)

print('------------------------------------------------>')

car =[ {
    'CarName' : "BMW",
    'carNo' : 31,
    'Colour' : 'black'
}]

for item in car:
    for a,b in item.items():
        print(a,b)

store = {
    'laptop':"HP",
    'Mobile':"Samsung",
    'EarPhone':'Boat',
    'Powerbank':'Syska'
}

store['Mobile']="iPhone"
store1 = store
print(store)
print(store1)

store1['EarPhone']="MI"

print(store)
print(store1)

print(store.get('Mobile'))

print('------------------------------------------------>')

#Methods

kiran = {
    'firstName':'Kiran',
    'lastName':"Dudhane",
    'age': 25,
    'colour':'fair',
    'skills':['javascript','python']
}

kiran.update({'age':'26'})        # to update the value
kiran.update({'colour':'brown'})
kiran.update({'mobile':'SAMSUNG'})    # to update add key and value to object
print(kiran)


kiran.popitem()     # remove the last key value set
print(kiran)

kiran.pop('colour')     # to remove the specific set with key name
print(kiran)

# kiran.clear()     # to clear the dictionary
# print(kiran)

kiran.setdefault('car','Nexon')     # to add default value in dictionary
print(kiran)

print('------------------------------------------------>')

a = ['name','Bdate','year','HEdu']
b = ['Kiran','20/02',1996,'BE']

print(dict.fromkeys(a,b))   # 1st array setv as keys...2nd  full array set as value of every key

kiran = {
    'firstName':'Kiran',
    'lastName':"Dudhane",
    'age': 25,
    'colour':'fair',
    'skills':['javascript','python']
}

for key in kiran:
    print(key,kiran[key])

kiran.update({"salary":"4LPA"})
print(kiran)

