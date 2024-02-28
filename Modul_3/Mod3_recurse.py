def test_print(a, b='параметр по умолчанию', *args, **kwargs):
    print('a:', a)
    print('b:', b)

    for arg in enumerate(args):
        print('поз параметр:', arg)

    for key, value in kwargs.items():
        print('имен параметр:', key, value)

poz_parametr=[2.4, 'qqqq']
dict_parametr={'key': 'param1', 'valve': 1}
# test_print('значение a', '20', *poz_parametr, **dict_parametr)
test_print(a = 'значение a', b = '20', *args = *poz_parametr, **kwargs = **dict_parametr)

#
#
#
# def factorial(n):
#     if n==1:
#         return 1
#     factorial_n_1 = factorial(n-1)
#     return n * factorial_n_1
#
# print('')
# find_factorial = 4
# print(find_factorial, '! = ',  factorial(find_factorial))


html_dom = {
    'html': {
        'head': {
            'title': 'колобок',
        },
        'body': {
            'h2': 'привет',
            'div': 'хочешь сказку?',
            'p': 'жили были'
        }
    }
}

def find_element(tree, element_name):
    if element_name in tree:
        return tree[element_name]
    for key, sub_tree in tree.items():
        if isinstance(sub_tree, dict):
            result = find_element(sub_tree, element_name)
            if result:
                break
    else:
        result = None
    return result

res = find_element(tree = html_dom, element_name = 'body')
print(res)

html_dom = {
    'html': {
        'head': {
            'title': 'колобок',
        },
        'body': {
            'h2': 'привет',
            'div': 'хочешь сказку?',
            'p': 'жили были'
        }
    }
}
def find_element(tree, element_name):
    if element_name in tree:
        return tree[element_name]
    for key, sub_tree in tree.items():
        if isinstance(sub_tree, dict):
            result = find_element(sub_tree, element_name)
            if result:
                break
