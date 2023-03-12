n = int(input('input'))

res = int(1)
if n != 0:
    while n != 1:
        res *= n
        n-=1    
print(res)