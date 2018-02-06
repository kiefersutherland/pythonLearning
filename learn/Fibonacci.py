

def fib_recur(n):
    assert n >= 0
    if n in (0, 1):
        return n
    return fib_recur(n - 1) + fib_recur(n - 2)

for i in range(30):
    print(fib_recur(i), end=" ")


def fib_loop(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

for i in range(20):
    print(fib_loop(i), end=" ")


import numpy

def fib_matr(n):
    return (numpy.matrix([[1, 1], [1, 0]]) ** (n - 1) * numpy.matrix([[1], [0]]))[0, 0]

for i in range(20):
    print(int(fib_matr(i)), end=" ")