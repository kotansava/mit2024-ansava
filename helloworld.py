print("Hello, world!")

def fib(n):
    seq = [0, 1]
    for i in range(2, n):
        nn = seq[-1] + seq[-2]
        seq.append(nn)

    for i in seq:
        print(i)
    

fib(10)
