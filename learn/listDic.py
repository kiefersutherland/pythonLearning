# -*- coding: utf-8 -*-
import os
c=[d for d in os.listdir('.')]
print(c)
#当前列表

t=[x * x for x in range(1, 11)if x % 2 == 0]
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(t)

#全排列
k= [m + n for m in 'ABCD' for n in 'WXYZ']
print(k)

#小写
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])


def f(x):
  return x * x
 
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))



#计算素数的一个方法是埃氏筛法
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

# 打印1000以内的素数:
for n in primes():
    if n < 100:
        print(n)
    else:
        break

#获得一个对象的所有属性和方法
print(dir('abc'))