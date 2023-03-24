def sum_fib(a):
    if a in [0,1]:
        return 1
    return sum_fib(a-2) + sum_fib(a-1)
print(sum_fib(int(input())))