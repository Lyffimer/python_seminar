values = [1, 23, 42, 'asdfg']

trasformation = lambda x: x
transformed_values = list(map(trasformation, values))

if values == transformed_values:
    print('ok')
else:
    print('fail')
