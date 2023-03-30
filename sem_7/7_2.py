


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
#orbits = [tuple(map(int, input.split())) for i in range(input('input qnt '))]

#print([max_1 for ind, val in enumerate(orbits) if ind != val if max_1 <(ind*val): max_1=(ind*val)])

def func(li):
    dict = {i[0]*i[1]: i for i in li if i[0]!= i[1]}
    return max(dict.items())[1]



print(*func(orbits))






#print(*find_farthest_orbit(orbits))


