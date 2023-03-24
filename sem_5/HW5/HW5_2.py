def stowage(a, b):
    if b < 0 < a:
        a, b = b, a
    if b == 0:
        return a
    return stowage(a + 1, b - 1)

num_1, num_2 = (int(input()), int(input()))
print(stowage(num_1, num_2))
