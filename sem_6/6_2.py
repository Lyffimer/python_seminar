# list_1 = [1, 2, 3, 4, 5]
# list_2 = [1, 5, 1, 5, 1]
# list_3 = []
# count_1 = 0
# n = int(input('введите кол во эл '))
# for i in range(n):
#     list_1.append(int(input('введите элемент')))


# for i in range(1, len(list_1)-1):
#     if (list_1[i] > list_1[i+1]) & (list_1[i] > list_1[i-1]):
#         count_1 += 1
# print(count_1)



list_1 = [1, 5, 1, 5, 1]

count_1 = 0
# n = int(input('введите кол во эл '))
# for i in range(n):
#     list_1.append(int(input('введите элемент')))


for i in range(1, len(list_1)-1):
    if list_1[i] == max(list_1[i-1:i+2]):
        count_1 += 1
print(count_1)

print(len([i for i in range(1, len(list_1)-1) if list_1[i] == max(list_1[i-1:i+2])]))

print(len([i for i in range(1, len(list_1)-1) if list_1[i-1] < list_1[i] > list_1[i+1]]))