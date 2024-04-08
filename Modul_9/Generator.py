
def all_variants(str_in):
    len_str = len(str_in)
    for i in range(len_str):
        yield str_in[i]

    for i in range(len_str):
        char = str_in[i]
        for ii in range(i+1, len_str):
            char += str_in[ii]
            if len(char) != len_str:
                yield char
    yield str_in

a = all_variants("abc")
for i in a:
    print(i)

# a
# b
# c
# ab
# bc
# abc


# # *********************************************************
# def fibonacci2(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a+b
#
# fib = fibonacci2(10)
# print(fib)
# for value in fib:
#     print(value)
#
# # *********************************************************
# def fibonacci3():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a+b
# for value in fibonacci3():
#     print(value)
#     if value > 10:
#         break
# # *********************************************************
# def fibonacci4():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a+b
#         if value > 10:
#             return
#
# for value in fibonacci4():
#     print(value)
#
# # *********************************************************
# def queue(*args):
#     data = list(args)
#     while data:
#         next = data.pop(0)
#         new_value = (yield next)
#         if new_value is not None:
#             data.append(new_value)
#
# shop_queue = queue('Arten', 'Marine', 'Vlad', 'Vasy')
# for name in shop_queue:
#     print(f'К кассе приглашается: {name}')
#     if name == 'Marine':
#         print('А кто последний?')
#         name = shop_queue.send('Margo')
#         print(f'К кассе приглашается: {name}')
#
