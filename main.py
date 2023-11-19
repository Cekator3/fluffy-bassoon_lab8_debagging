def array_sort(arr):
    if not isinstance(arr, list):
        raise Exception('Array expected but ' + type(arr) + ' given')
    for i in range(0, len(arr) - 1):
        smallest = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest]:
                smallest = j
        arr[i], arr[smallest] = arr[smallest], arr[i]

def Polindrom(s):
    reversedString = ''.join(reversed(s))
    return s == reversedString

def fac(n):
    if n < 0:
        raise Exception("Нету отрицательного факториала")
    if n <= 1:
        return 1
    return (n * fac(n - 1))

def fib(n):
    if n < 1:
        raise Exception("Нету отрицательного ряда")
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)

def step(a, b):
    return a ** b

def prost(x):
    for i in range(2, x // 2+1):
        if (x % i == 0):
            return False
    return True
