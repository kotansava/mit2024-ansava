print("Hello, world!")

def fib(n):
    if n-1 <= 0:
        return 0
    elif n-1 in (1, 2):
        return 1
    return fib(n - 1) + fib(n - 2)

def cycle_fib(n):
    for i in range(n+1):
        print(fib(i))


cycle_fib(10)