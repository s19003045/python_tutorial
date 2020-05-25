'''
主題：data type
'''

# Numbers
print('=========Numbers=======')
myInt = 10
print(type(myInt))  # <class 'int' >

myFloat = 10.111
print(type(myFloat))   # <class 'float' >

myFloat = 7.5e2
print(type(myFloat))   # <class 'float' >

myComplex = 5 + 5j
print(type(myComplex))   # <class 'complex' >

addition = 10 + 9
print(addition)   # 19

substraction = 20.0 - 10.1
print(substraction)   # 9.9

multiplication = myInt * 15
print(multiplication)   # 150

division = 99 / 8
print(division)   # 12.375

# using constructor
price = int(10.5)
print(price, " belongs to ", type(price))   # 10  belongs to < class 'int' >

price = float(10)
# 10.0  belongs to < class 'float' >
# (5.5+0j)  belongs to < class 'complex' >
print(price, " belongs to ", type(price))

price = complex(5.5)
print(price, " belongs to ", type(price))

price = complex(2, 3)
# (2+3j)  belongs to < class 'complex' >
print(price, " belongs to ", type(price))


# operation
num1 = 10
num2 = 20
num3 = 55
print('Initial:', num1, num2, num3)

num1 *= 2
num2 **= 2
num3 /= 5
print('round 2:', num1, num2, num3)


# logical operators
print(1 == 2)   # False
print(3 > 0)   # True
print(4 != 3.0)   # True
print(3 > 1 and 2 == 2)   # True
print(3 > 1 or 4 < 2)   # True
print(not(True))   # False

# identity operators
applePrice = 10
bananaPrice = 20
print(applePrice is bananaPrice)   # False
print(applePrice is not bananaPrice)   # True

# membership operators
msg = 'Hello world'
print('hell' in msg)  # False
print('hello' in msg)  # False
print('Hello world' in msg)   # True
print('good' not in msg)   # True
print('a' in ['a', 'b', 'c'])   # True
print('ab' in ['a', 'b', 'c'])  # False

print('=========Strings=======')
