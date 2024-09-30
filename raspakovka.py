def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params('str', 2)
print_params(False)
print_params()

print_params(b = 25)
print_params(c = [1,2,3])



values_list = ['str', 43, False]
values_dict = {'a': 'str', 'b': False, 'c': 3}


print_params(*values_list)
print_params(**values_dict)


values_list_2 = [2.0, 'apple']
print_params(*values_list_2, 42)