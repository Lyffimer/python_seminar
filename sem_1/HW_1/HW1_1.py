numb = int(input('Введите число '))

summ = 0
while numb != 0:
    summ = summ + (numb%10)
    numb = numb//10
print('Сумма чисел равна:', summ)