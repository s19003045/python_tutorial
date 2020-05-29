'''
主題：function, lambda
'''
# ======function======
# parameter


def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


print(addition(3, 5))   # 8
print(subtraction(10, 3))   # 7
print(multiplication(4, 2))   # 8
print(division(10, 5))   # 2.0


# so many parameter
def children(*kids):
    print(kids)
    for kid in kids:
        print(kid)


kids = ['john', 'mary', 'peter']

print(children(kids[0], kids[1], kids[2]))
# ('john', 'mary', 'peter')
# john
# mary
# peter
# None (代表沒有回傳值)


def children2(**kids):
    print(kids)
    for kid in kids:
        print(kid)


print(children2(kids=kids))
# {'kids': ['john', 'mary', 'peter']}
# kids
# None (代表沒有回傳值)


# Default Parameter Value
def saySomething(msg='hello'):
    print(msg)


print(saySomething('good job'))
# good job
# None
print(saySomething())
# hello
# None


# The pass Statement
def walkThrough():
    pass


print(walkThrough())  # None


# recursive function
def recursion(n):
    if n > 0:
        print(n)
        n = n - 5
        recursion(n)


recursion(100)

# 上面函式相當於：
for v in range(100, 0, -5):
    print(v)

# ======lambda========
# lambda : small anonymous function
#　x = lambda a: a + 10
# 上面的 lambda 匿名函式儲存後會自動轉成下面


def x(a): return a + 10


print(x(5))  # 15


# x = lambda a, b : a * b
# 上面的 lambda 匿名函式儲存後會自動轉成下面

def x(a, b): return a * b


print(x(5, 6))  # 30


# when to use lambda
def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)

print(mydoubler(11))  # 22
