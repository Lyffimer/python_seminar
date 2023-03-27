count1 = int(input())
list1 = []
for _ in range(count1):
    list1.append(int(input()))
count2 = int(input())
list2 = []
for _ in range(count2):
    list2.append(int(input()))

print([x for x in list1 if x not in set(list2)])