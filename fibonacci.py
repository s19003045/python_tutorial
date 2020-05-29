# 費氏數列
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


# function
def fibonacci(n):
    res = []
    a, b = 0, 1
    while a < n:
        res.append(a)
        a, b = b, a + b
    else:
        print(res)
        print('that\'s all')


fibonacci(10000)
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
# that's all


# class
class Math:
    def __init__(self, name):
        self.name = name

    def fibonacci(self, n):
        res = []
        a, b = 0, 1
        while a < n:
            res.append(a)
            a, b = b, a + b
        else:
            print(res)
            print('that\'s all')


fibo = Math('fibo')
fibo.fibonacci(10000)
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
# that's all
