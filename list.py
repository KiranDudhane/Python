# collections--------> string, array, list, dictionary, tuple, set array

# list store the values by Index

fruits = ['mango', 'Banana', 'Strawberry', 'Chiku', 'jackfruit', "Banana"]

for item in fruits:
    print(item)

for item in range(len(fruits)):
    print(fruits[item])

# printing last element of the list
print(len(fruits)-1)
print(fruits[(len(fruits)-1)])

fruits.append('grapes')    # add ele at last of list
print(fruits)

fruits[3] = "orange"    # replace the element with index no
print(fruits)

# if item is not include shows error......last index not inlcuded
a = fruits.index("Banana", 2, 6)
print(a)

print('----------------------------------------------->')

flowers = ['rose', 'lily', 'sunflower', 'marigold']

# userinput = input('enter the flower you want ')

# for flower in flowers:
#     if userinput == flower:
        
#         print('!!! flower is available')
#     if userinput != flower:
        
#         print('flower is not available')

print('rose' in ['rose', 'lily', 'sunflower', 'marigold'] )


flowers[2] = "lotus" 
flowers1 = flowers

print (flowers)
print(flowers1)    # new memory created and any changes in it changes in both old as well as new

flowers1[0] = 'musterd'
print (flowers)
print(flowers1)

flowers2 = flowers1.copy()

flowers2[1] = 'ostrich'

print (flowers2)   # at copy we can not chnage previous list data
print(flowers1)

flowers2.clear()     # blank [] cause clear the list
print(flowers2)

del flowers1
# print(flowers1)             # not define cause deleted the list

print('----------------------------------------------->')

vehical = ['car','Cycle','Motorbike','scooter']
vehicalA = ['bullcart','BMW','BUS','LuxeryCar']

# vehical.extend(vehicalA)
# print(vehical)
# vehicalA.extend(vehical)    # for to add tow list
# print(vehicalA) 

vehical.insert(3,"Airoplane")    # to insert the value at place of index n old value push to next index
print(vehical)


vehical.sort()
print(vehical)    # sort from A-Z and then a-z


vehicalA.pop()
print(vehicalA)    # to remove the last element

vehical.pop(2)    # to remove the element at index 2
print(vehical)

vehicalA = ['bullcart','BMW','BUS','LuxeryCar']

# vehicalA.remove('BUS')      # if index is unknown then we use remove method
# print(vehicalA)

vehicalA.reverse()    # for reverse the list
print(vehicalA)


num = [45,12,7,96,34,20,98]

num.sort()
print(num)

num.reverse()
print(num)

print('----------------------------------------------->')

listA = ['mango','grapes','Banana','Strawberry', 'Blackberry', 'Orange']    

for items in listA:
    print(items)

for items in range(len(listA)):
    print(listA[items])










