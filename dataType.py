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
msg = 'GoToSchool'
print(msg[2:])   # ToSchool
print(msg[:3])   # GoT
print(msg[1:4])   # oTo
print(msg[-4:-1])  # hoo
print('len:', len(msg))  # len: 10


# string method
msg = '  Good job ! John'

# split()
print(msg.split())  # ['Good', 'job', '!', 'John']
print(msg.split('!'))   # ['  Good job ', ' John']
print(msg)  # Good job ! John  => 連同最前面的空格也會印出來

# strip()
print(msg.strip())   # Good job ! John  => 把前後的空格挪去
print(msg)

# lower()  & upper()
print(msg.lower())   # good job ! john
print(msg.upper())  # GOOD JOB ! JOHN

# in & not in
print('Go' in msg)   # True
print(' ' in msg)   # True
print('Tom' not in msg)   # True
print('ooo' in msg)  # False

a = 'hello'
b = 'world'
c = a + ' ' + b
print(c)  # hello world

# string format
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."

print(myorder.format(quantity, itemno, price))
# I want 3 pieces of item 567 for 49.95 dollars.


# count()：某字元出現次數
msg = 'banana is delicious'
print(msg.count('a'))  # 3
print(msg.count('an'))  # 2

# capitalize()：頭大寫
print(msg.capitalize())  # Banana is delicious

# find()
print(msg.find('i'))   # 7
print(msg.find('ba'))   # 0
print(msg.find('an', 2, 8))  # 3

# index() ： 與 find() 的用法一樣
print(msg.index('i'))   # 7
print(msg.index('ba'))   # 0
print(msg.index('an', 2, 8))   # 3


# isnumeric()
msg = '123456'
print(msg.isnumeric())  # True
msg = '1234abc'
print(msg.isnumeric())  # False

# isalpha()
print(msg.isalpha())   # False
msg = 'abc'
print(msg.isalpha())   # True

# isdigit()
msg = '1234'
print(msg.isdigit())   # True
msg = 'abc'
print(msg.isdigit())   # False
msg = '123abc'
print(msg.isdigit())   # False

# join()
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)   # John#Peter#Vicky

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x)  # nameTESTcountry
y = mySeparator.join(myDict.keys())
print(y)  # nameTESTcountry
z = mySeparator.join(myDict.values())
print(z)   # JohnTESTNorway

# =====Boolean=======
print(bool(3 > 2))   # True
print(bool(3 != 2))   # True
print(bool(3 == 2))   # False

# print(bool(3 > '2'))
# TypeError: '>' not supported between instances of 'int' and 'str'

# 轉換後再比大小
print(bool(3 > int('2')))  # True

# 大部分都可是 True
print(bool('hello'))   # True
print(bool(15))  # True
print(bool(["apple", "cherry", "banana"]))


# 部分會判斷成 False
print(bool(0))   # False
print(bool(''))   # False
print(bool(None))   # False
print(bool([]))   # False   # False
print(bool(()))   # False
print(bool({}))   # False


def isBool():
    return True


print(isBool())   # True


def isGreater(a):
    if a > 3:
        return True
    else:
        return False


print(isGreater(5))  # True


# ====== Operator ========
# Logical Operators
print(True and False)   # False
print(True and True)  # True
print(True or False)  # True
print(False or True)  # True

# Bitwise operators(二位元運算)
x = 1
y = 4
# &  =>  Sets each bit to 1 if both bits are 1
# |  =>  Sets each bit to 1 if one of two bits is 1
x = x & 3   # 相當於 x &= 3
y = y | 3   # 相當於 y |= 3

print(x)   # 1
print(y)   # 7

x = 0
y = 0
x = x & 3
y = y | 3

print(x)   # 0
print(y)  # 3


# Identity Operators
print('is' is 'is')   # True
print('is' is 'hello')  # False
print('is' is not 'hello')   # True

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
# returns True because z is the same object as x

print(x is y)  # 嚴格比較
# returns False because x is not the same object as y, even if they have the same content

print(x == y)  # 鬆散比較
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y


# Membership Operators
print('is' in 'John is boy')  # True
print('is' not in 'afternoon')  # True
print(1 in [1, 2, 3, 4, 5])  # True
print(1 in (1, 2, 3, 4, 5))  # True
