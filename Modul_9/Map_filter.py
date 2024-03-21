def odd(x):
    return x % 2
def sqr(x):
    return x ** 2


my_number = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

res = map(sqr, filter(odd, my_number))
print(list(res))