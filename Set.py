    # Set- To store the unique value ----does not store the value by index

setA = {1,3,4,5,75,8,94,6}
print(setA)

print(type(setA))

for k in setA:
    print(k)

# Methods:

setA.remove(75)      # to remove the element
print(setA)

setA.pop()     # to remove 1st ele
print(setA)

setA.clear()     # to clear all ele in set
print(setA)

del setA       # to del the set
# print(setA)

print('---------------------------------------->')

setB= {11,22,33,44,55,66}

setB.update([88,99,33])    # to aad the ele in set,,,,give an in (),[],{},'',""
print(setB)

setB.update("Kiran")
print(setB)

setB.update({1,2,3})
print(setB)

setC = {15,23,46,78,94}

setD = setC.copy()      # copy the set any change in set cant throughout

print(setC)
print(setD)

setC.remove(78)
print(setC)
print(setD)

setD.remove(23)
print(setC)
print(setD)

setE = {78,89,54,62}    

setF = setE      # when set is assign to other...single change in any one of them can change both sets

setF.remove(89)
print(setE)
print(setF)

setE.remove(62)
print(setE)
print(setF)

print('----------------------------------------------------->')

setG = {1,5,47,89,45,25,14}
setH = {14,25,36,87,45,5}


# print(setG.difference(setH))    # to find different ele from other set
# print(setH.difference(setG))

# setG.difference_update(setH)
# print(setG)
# setH.difference_update(setG)
# print(setH)

# print(setH.intersection(setG))     # to find common ele of both sets
# print(setH)
# print(setG)

# setH.intersection_update(setG)     # to find common ele of both sets
# print(setH)

# setG.intersection_update(setH)     # to find common ele of both sets
# print(setG)

setG.add(99)              # to add element in set
print(setG)

setH.discard(36)        # to remove the element from set
print(setH)

print('----------------------------------------------------->')

setI = {1,2,3,4}
setJ = {5,6,7,8}

setK = {2,3,4}

# print(setK.issubset(setI))     # to check another set is sub set of other T/F
# print(setK.issubset(setJ))

# print(setI.issuperset(setK))    # to check another set is supper set of other T/F
# print(setJ.issuperset(setK))

# print(setI.union(setJ))            # to join two set

# print(setK.symmetric_difference(setJ))  # to join with and symmetric element

# setI.symmetric_difference_update(setK)   # to find out symmetric element form both set
# print(setI)

# print(setI.isdisjoint(setJ))    # no common ele in both set then is says true

setI = {1,2,3,4}
setJ = {5,6,7,8}

for v  in setI:
    print(v)

# for B in range(len(setJ)):     # this loop can not work because ele not store by index
#     print(setJ[B])  



