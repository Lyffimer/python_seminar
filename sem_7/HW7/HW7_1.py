dictionary = 'УЕЫАОЭЯИЮЁ'
poetry = input().split()
sum_1 = []
# sum_2 = 0
for word in poetry:
    sum_2 = 0
    for j in word:
        if j.upper() in dictionary:
            sum_2 +=1
    sum_1.append(sum_2)
# print(sum_1)

if all(sum_1) and len(set(sum_1)) == 1:
    print("Парам пам-пам")
else:
    print("Пам парам")



# dictionary = 'аоуэыяеёюи'
# poem = input().split()
# result = [sum([True for j in word if j.upper() in dictionary]) for word in poem]
# print(result)
# if all(result) and len(set(result)) == 1:
#     print("Парам пам-пам")
# else:
#     print("Пам парам")
