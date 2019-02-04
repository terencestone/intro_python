def fib():
    a, b = 0, 1  # Multiple variable assignment
    for i in range(10):
        print(a)
        a, b = b, a + b

fib()