def exponent(num_1, num_2):
    if num_2 == 0:
        return 1
    if num_2 < 0:
        return exponent(num_1, num_2 + 1) * 1 / num_1
    return exponent(num_1, num_2 - 1) * num_1


print(exponent(int(input('Введите основание: ')), int(input('Введите степень: '))))