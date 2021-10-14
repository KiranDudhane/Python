name = "Kiranrkiran"
a = name.lower()
print(a)

b = name.upper()
print(b)

c = name.lower().upper()
print(c)


d = name.capitalize()   # 1st letter capitalies
print(d)

e = name.count('a')   # count the char in string
print(e)

f = name.index('r')   # find index of char in string
print(f)

g = name.index('r',3,6)   # last value not allowed     2nd occurance with known index value
print(g)

print('------------------------------->')

str = 'Strawberry'

h = str.index('r',(str.index('r')+1))    # 2nd occurance
print(h)

i = str.index('r',str.index('r',(str.index('r')+1))+1)    # 3rd occurance
print(i)


for char in range(len(str)):     # to find location and char in string
    if str[char] == 'r':
        print(char,str[char])

print('------------------------------->')

fruit = "Mango564"

print(fruit.isupper())  # check all upper case-----> T/F
print(fruit.islower())   # check all lower case-----> T/F
print(fruit.isnumeric())   # check all number is there-----> T/F
print(fruit.isalpha())    # check all alphabetes are there-----> T/F
print(fruit.isalnum())   # check all alpha- numeric are there-----> T/F
print(fruit.istitle())  # check 1st char is uppper or not-----> T/F



city = "nagpur"
print(len(city))

print(city[5])

fruits= "banana"
print(fruits.count('na'))   # count is applicable for substring also

print('------------------------------->')

print(fruits[1:3])
print(fruits[1:4])
print(fruits[2:5])    # last index not included
print(fruits[3:6])
print(fruits[-1:4])   # no output----------- start index always ahead from end index
print(fruits[1:-4])
print(fruits[1:-2])

print('------------------------------->')

Country = "India"

for cha in Country:
    print(cha)

for char in range(len(Country)):
    print(Country[char])    

print(Country.lower().count('i'))



country = "America".lower()

count = 0
for ch in range(len(country)):
    if country[ch] == 'a':
        count = count + 1
print(count)


# odd Numbers

for x in range(1,100,2):
    print(x)

# odd Numbers

for x in range(2,100,2):
    print(x)

for x in range(1,100):
    if x % 2 == 0:
        print(x)
