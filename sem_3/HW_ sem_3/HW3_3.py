ang_dict = {"AEIOULNSTRАВЕИНОРСТ": 1, "DGДКЛМПУ": 2,
            "BCMPБГЁЬЯ": 3, "FHVWYЙЫ": 4, "KЖЗХЦЧ": 5,
            "JXШЭЮ": 8, "QZФЩЪ": 10}

word = input()

count = 0
for i in ang_dict.items():
    for j in word.upper():
        if j in i[0]:
            count +=i[1]
print(count)


# print(sum([i[1] for i in ang_dict.items() for j in word.upper() if j in i[0]]))