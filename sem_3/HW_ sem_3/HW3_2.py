# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X

from random import randint

list_number = [randint(1, 21) for _ in range(int(input()))]

print(list_number)
number = int(input())
right_num = list_number[0]

for i in list_number:
    if abs(number - i) < abs(number - right_num):
        right_num = i

print(right_num)
