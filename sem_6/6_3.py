from time import time
from random import choices

# nums = [int(i) for i in input().split()]
nums = choices(range(3000), k=2000)

start = time()
m_dict = {}.fromkeys(nums, 0)

for j in nums:
    m_dict[j] += 1

num_count = [i // 2 for i in m_dict.values() if not i % 2]
print(sum(num_count))


print(time() - start)




# list_1 = [1,2,3,4,2,3,4,3,5,6,5,3,5,3,5,5]
# # list_2 = list(set(list_1))
# # count1 = 0
# # print(list_2)
# # for i in range(len(list_2)):
# #     count1 += list_1.count(list_2[i])//2
# # print(count1)

# dict_list = {}.fromkeys(list_1, 0)

# for i in list_1:
#     dict_list[i] += 1
# print(dict_list)
# print(sum([i//2 for i in dict_list.values() if not i%2 ]))


