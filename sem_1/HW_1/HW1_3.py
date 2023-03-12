# ticket = input('Введите номер биета ')

# if int(ticket[0]) + int(ticket[1]) + int(ticket[2]) == int(ticket[3]) + int(ticket[4]) + int(ticket[5]):
#     print('Билетик счастливый!')
# else:
#     print('Билет как билет(')


ticket_number = int(input())

sum_first = 0
sum_last = 0

while ticket_number:
    digit = ticket_number % 10
    if ticket_number > 999:
        sum_first += digit
    else:
        sum_last += digit
    ticket_number //= 10

print(f"The ticket is lucky: {sum_first == sum_last}")
