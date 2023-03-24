# def reorder(number, step=1, val1=0):
#     if step == number:
#         val1 = input("введите")
#         print(val1, end=" ")
#     else:
#         val1 = input(f"Введите")
#         reorder(number, step+1, val1)
#         print(val1, end=" ")

def reorder(number):
    if number == 0:
        return ""
    strochechka = input()
    return reorder(number - 1) + strochechka


nums = int(input("колл"))


print(reorder(nums))