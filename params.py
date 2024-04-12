def print_params(a = 1, b = 'Yes', c = True):
    print(a, b ,c)

print('''
Фунция с параметрами по умолчанию:
''')
print_params()
print_params(False, 5)
print_params(b = 25)
print_params(c = [1, 2, 3])

print('''
Распаковка параметров:
''')

values_list = [15, False, 'Banana']
values_dict = {'a': True, 'b': 'Book', 'c': 999}

print_params(*values_list)
print_params(**values_dict)

print('''
Распаковка + отдельные параметры:
''')


values_list_2 = [False, 'Moon']

print_params(*values_list_2, 42)