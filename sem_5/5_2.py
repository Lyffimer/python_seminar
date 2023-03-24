# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.

import random
n = int(input())

list_1 = [random.randint(1,5) for i in range(n)]
print(list_1)

num_min = min(list_1)
num_max = max(list_1)

# print([num_min if i == num_max else i  for i in list_1])

def Thing(List, x):
    if List[x] == num_max:
        List[x] = num_min
    if x == 0:
        return List
    else:
        return Thing(List, x-1)

print(Thing(list_1, len(list_1)-1))