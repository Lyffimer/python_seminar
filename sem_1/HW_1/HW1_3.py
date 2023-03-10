ticket = input('Введите номер биета ')

if int(ticket[0]) + int(ticket[1]) + int(ticket[2]) == int(ticket[3]) + int(ticket[4]) + int(ticket[5]):
    print('Билетик счастливый!')
else:
    print('Билет как билет(')