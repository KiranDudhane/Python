
# class student :
#         age = 10
#         name = 'Kiran'
#         language  = 'Marathi'

#         def display(self):
#             print(self.name)

# kiran = student()
# kiran.display()

# print(kiran.age)
# print(kiran.language)

# kiran.age = 25
# print(kiran.age)             # get updated value

# suraj = student()
# print(suraj.age)                        #get set value


# class vehical:
#     def __init__(self,brdnm,clr,pz):
#         self.BrandName =  brdnm
#         self.colour = clr
#         self.Prize = pz

#     def display(self):
#         print(self.BrandName,self.Prize)


# Car = vehical('BMW','Black','1core')
# bike = vehical('KTM','orange','2Lac')

# Car.display()
# bike.display()

# print('------------------------------------------->')

# class Bank :
#     def __init__(self,accNo,accName,bal):
#         self.AccountNumber = accNo
#         self.AccountName = accName
#         self.Balance = bal

#     def deposit(self,amount):
#         self.Balance = self.Balance + amount

#     def Withdraw(self,amount):
#         if amount < self.Balance:
#             self.Balance = self.Balance - amount
#         else:
#             print('Insufficient Balance')

# Kiran = Bank(123,"Saving",10000)

# Kiran.Withdraw(500)
# print(Kiran.Balance)

# Kiran.deposit(1000)
# print(Kiran.Balance)

# print('-------------------------------------------------------------->')

# # 18/09/2020 sub :- class2

# # program 01

# class student:
#     def __init__(self):                      # hardcore value
#         self.name = 'kiran'
#         self.age = 25
#         self.marks = 90

#     def info(self):
#         print('My name is ' + self.name)
#         print('My age is ' + str(self.age))
#         print('My marks are ' + str(self.marks))


# kiran = student()
# kiran.info()

# # program 02

# class student:                                    # with constructor
#     def __init__(self,nm,ag,mks):
#         self.name = nm
#         self.age = ag
#         self.marks = mks

#     def info(self):
#         print('My name is ' + self.name)
#         print('My age is ' + str(self.age))
#         print('My marks are ' + str(self.marks))


# kiran = student('Kiran',26,89)
# kiran.info()

# kiran.language = 'Marathi'
# print(kiran.language)

# # Program 03

# class Vehical:
#     def __init__(self, brand = '', clr = 0):   # if default is not set then method without arguments shows error
#         self.Brandname = brand
#         self.Colour = clr

#     def display(self):
#         print('Brand',self.Brandname)
#         print('My colour', self.Colour)

# s = Vehical()
# s.display()

# f = Vehical('BMW','Navy Blue')
# f.display()

# print('------------------------------------------>')


# # HW - Problem 04

# #class  ----> 4

# # name
# # age
# # language
# # adharNo


# # 4 Objects --->
# # Reference variable only one
# # loop ---
# # # name
# # # age
# # # language
# # # adharNo

# # use constructor to set the values - 4 min

# class Employee:
#     def __init__(self,nm,ag,lan,idN):
#         self.name = nm
#         self.age =  ag
#         self.language = lan
#         self.Aaddhar = idN

#     def EMP(self):
#         print('Employee name is ' + self.name)
#         print('its age is ' + str(self.age))
#         print('known language is ' + str(self.language))
#         print('Aaddhar number is ' + str(self.Aaddhar))
#         print('------------------------------------------_>')


# # kiran = Employee('Kiran',25,'Hindi',789)
# # kiran.EMP()

# listA = [Employee('Kiran',25,'Hindi',789),Employee('Suraj',20,'Marathi',89),Employee('Tejal',18,'Marathi',489),Employee('Sagar',29,'Hindi',947)]

# for Emp in listA:
#     Emp.EMP()


# # 20/09/2021       -----------class

# # Program 05

# class car:
#     #class variable   / Instance Varible

#     madeIn = "India"

#     def __init__(self,Brand,Clr,regNo):
#         self.Brand = Brand
#         self.Colour = Clr
#         self.regiNo = regNo

# audi = car("Audi",'Black',1245)
# Bmw = car('BMW','Blue',789)
# Tata = car('Tata','Gray',2563)

# print(audi.madeIn)
# audi.madeIn = "USA"
# print(audi.madeIn)

# print(Bmw.madeIn)
# print(Tata.madeIn)

# # Program 06

# class sample:
#     def __init__(self):
#         self.x = 10
#     def modify(self):
#         self.x = self.x + 10

# a = sample()
# b =  sample()

# print(a.x)  #10
# print(b.x)   #10

# a.modify()

# print(a.x)  #20
# print(b.x)   #10


# # program 07

# class car:
#     madeIn = "India"

#     @classmethod
#     def modify(cls):
#         cls.madeIn = "USA"

#     def __init__(self,Brand,Clr,regNo):
#         self.Brand = Brand
#         self.Colour = Clr
#         self.regiNo = regNo

# audi = car("Audi",'Black',1245)
# Bmw = car('BMW','Blue',789)
# Tata = car('Tata','Gray',2563)

# # audi.modify()    # this not work cause modify method apply for class
# car.modify()      # class calling methods

# print(audi.madeIn)
# audi.madeIn = "INDIA"
# print(audi.madeIn)

# print(Bmw.madeIn)
# print(Tata.madeIn)

# print('---------------------------------------->')
# # program 08

# class student:
#     def __init__(self, n = '', m = 0):
#         self.name = n
#         self.marks = m

#     def display(self):
#         print('Student name is ' + self.name)
#         print('Students marks are ' + str(self.marks))
#         print('----------------------------------------->')

#     def Grade(self):
#         if self.marks >= 65 and self.marks < 100:
#             print('Destingtion')
#         elif self.marks >= 50 and self.marks < 65:
#             print("GoodClass")
#         elif self.marks >= 35 and self.marks < 50:
#             print("PassClass")
#         else:
#             print("Fail")


# ListB = [student('Kiran',64),student('suraj',68),
#         student('Tejal',54),student('sagar',45),student('ram',32)]

# for s in ListB:
#     s.display()

# for std in ListB:
#     std.Grade()

# 20/09/2021----------------------------------->

# class Car:

#         madein = 'India'

#         @classmethod
#         def modify(cls):
#             cls.modein = "Japan"

#         def modifyl(self):
#             self.madein = "China"

#         def __init__(self,clr,type,regNo):
#             self.colour = clr
#             self.type = type
#             self.regNo =  regNo

# audi = Car('Black','SUV',123)
# BMW = Car('Blue','Sedane',789)
# TATA = Car('White',"Nexon",459)

# print(audi.madein)
# audi.modifyl()

# print(audi.madein)

# Car.modify()
# print(audi.madein)
# print(TATA.madein)
# print(BMW.madein)







