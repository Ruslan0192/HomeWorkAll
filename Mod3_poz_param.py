

def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(2,'')
print_params(b = '45', c = False)
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = ['qwe', 2, False]
values_dict = {'c': 'qwe1', 'a': 3, 'b': True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [5, 'port']
print_params(*values_list_2, 42)
