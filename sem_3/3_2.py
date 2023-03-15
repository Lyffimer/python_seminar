list_1 = [1,2,3,4,5]

k = int(input())
print(list_1)

for i in range(k):
    list_1.insert(0, list_1[- 1])
    #list_1.insert(0, list_1.pop(-1))
    list_1.pop()
    print(list_1)