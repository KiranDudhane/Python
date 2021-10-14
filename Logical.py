# Prob 01
fruit = "Strawberry"
# o/p  ------>{
#   'S':1,
    # 't':1,
    # 'r':3,
    # .
    # .
# }
j={}
for char in fruit:
    j[char] = j.get(char,0) + 1

print(j)

# Prob 02

Num = [11,22,33,44,55,88,-4,-21,78,9]
# find Max or min no from array
max = Num[0]
min = Num[0]

for D in Num:
    if D < max:
        max = D
    elif D > min:
        min = D
print(max)
print(min)

# Prob 03

inputA = "4a3b2c"

rev = ""

for x in range(len(inputA)):
    if x % 2 == 0:
        num = int(inputA[x])
        #print(num)
        rev =  rev + num * (inputA[x+1])
print(rev)

# HW - Problem 04

#class  ----> 4

# name
# age
# language
# adharNo


# 4 Objects --->
# Reference variable only one
# loop ---
# # name
# # age
# # language
# # adharNo

# use constructor to set the values - 4 min

class Employee:
    def __init__(self,nm,ag,lan,idN):
        self.name = nm
        self.age =  ag
        self.language = lan
        self.Aaddhar = idN

    def EMP(self):
        print('Employee name is ' + self.name)
        print('its age is ' + str(self.age))
        print('known language is ' + str(self.language))
        print('Aaddhar number is ' + str(self.Aaddhar))
        print('------------------------------------------_>')


# kiran = Employee('Kiran',25,'Hindi',789)
# kiran.EMP()

listA = [Employee('Kiran',25,'Hindi',789),Employee('Suraj',20,'Marathi',89),Employee('Tejal',18,'Marathi',489),Employee('Sagar',29,'Hindi',947)]

for Emp in listA:
    Emp.EMP()