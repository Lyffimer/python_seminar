# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k ), не превосходящие числа N.


N = int(input('Введите число '))
count = 1
for i in range(N):
    if count > N:
        break
    print(count, end=" ")
    count *=2
    
    

