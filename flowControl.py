'''
主題：flow control
- if
- for
- while
'''

import datetime  # 載入 datetime 模組

# Flow Control

# if
# oneline if
print('----- if: oneline if------')
if 3 > 1:
    print('3 is bigger than 1.')

# example: check number can be divided by a, b
print('----- if: check number can be divided by a, b------')
myNumber = 15
if myNumber % 15 == 0:
    print(myNumber, 'can be divided by', 15)
elif myNumber % 5 == 0:
    print(myNumber, 'can be divided by', 5)
elif myNumber % 3 == 0:
    print(myNumber, 'can be divided by', 3)
else:
    print(myNumber, 'can not be divided by 3 or 5.')


# example: check word in sentence
print('----- if: check word in sentence------')
if 'hello' in 'hello, world':
    print('"hello" is in the sentence')
else:
    print('"hello" is not in the sentence.')


# example: compare two days
print('----- if: compare two days ------')
today = datetime.datetime.now()
someDay = datetime.datetime(2020, 7, 1)
print('today:', today)
if today > someDay:
    print('today is before', someDay)
elif today == someDay:
    print('two day are the same day')
elif today < someDay:
    print('today is after', someDay)
else:
    print('can\'t define two day')

print('-----for loop over list-----')
# for loop over list
fruits = ['apple', 'banana', 'water lemon']
for fruit in fruits:
    print(fruit, len(fruit))

print('-----for loop over tuple------')
# for loop over tuple
days = ('Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday', 'Sunday')
for day in days:
    print(day)

print('-----for loop over string------')
# for loop over string
message = 'My friend, congratulations.'
for letter in message:
    print(letter, end=',')
print('\n')

print('-----for loop over number------')
# for loop over number
for n in range(10):  # 印出 0 ~ 9
    print(n)

print('-----------')
for n in range(1, 5):  # 印出 0 ~ 4
    print(n)

print('-----------')
for n in range(10, 2, -2):  # 印出： 10 8 6 4
    print(n)


# for loop over set
print('-----for loop over set------')
numbers = {100, 200, 300, 400}
for num in numbers:
    print(num)

# for loop over dictionary
print('-----for loop over dictionary------')
personalInfo = {
    'name': 'John',
    'age': 18,
    'city': 'Taipei'
}
for key in personalInfo:
    print(key)

# name
# age
# city

for key, val in personalInfo.items():
    print(key, val)

# name John
# age 18
# city Taipei


# while loop
print('=======while loop=====')


# example: 費氏數列
print('=======while loop=====')
a, b = 0, 1  # 多重賦值
while a < 1000000:
    print(a, end=',')
    a, b = b, a + b  # 多重賦值:右項運算 (expression) 會先被計算 (evaluate)，賦值再發生
# 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765,10946,17711,28657,46368,75025,121393,196418,317811,514229,832040,

print('==========')
# 或者可以如下表示：
a, b = 0, 1
while a < 1000000:
    print(a, end=',')
    a0 = a
    a = b
    b = a0 + b
# 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765,10946,17711,28657,46368,75025,121393,196418,317811,514229,832040,

print('==========')
# 錯誤寫法：(不如預期)
a, b = 0, 1
while a < 1000000:
    print(a, end=',')
    a = b  # a 被賦值 b 的值
    b = a + b  # 此時的 a 的值已是新的 a值 ，而不是原本的 a值
# 0,1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,
print('==========')
