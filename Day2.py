
def addA(a, b):
    return a + b
    print("Hello")


r = addA(12, 13)
print(r)

x = 10
print(type(x))


def addB(q, w):
    return "Hello"


print(addB(10, 10))

name = "Kiran"
print(type(name))

print(name[0])
print(name[-1])

print('----------------------------------------->')

for char in name:
    print(char)

print('----------------------------------------->')

for x in range(10):
    print(x)

print('----------------------------------------->')

for x in range(20, 50):
    print(x)

# range(start value, end value(execute till end value -1), step(joint default 1))

for x in range(10, 50, 5):
    print(x)

string = "Kiran Dudhane"

print(len(string))

for char in range(len(string)):
    # print(char)
    print(string[char])


# h = "book"
# g = {}

# for char in h:
#     # print(char)
#     g[char] = g.get(char, 0) + 1
#     print(g)
