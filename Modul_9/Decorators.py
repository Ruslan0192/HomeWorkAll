
def is_prime(func):
    def wrapper(*args):
        a = func(*args)
        k = 0
        for i in range(2, a // 2 + 1):
            if (a % i == 0):
                k = k + 1
        if (k <= 0):
            print("Простое")
        else:
            print("Составное")
        return a
    return wrapper

@is_prime
def sum_three(*args):
    summa = 0
    for i in args:
        summa += i
    return summa


result = sum_three(2, 3, 6)
print(result)



# import time
#
# def time_track(func):
#     def surrogate( *args, **kwargs):
#         started_at = time.time()
#         result = func(*args, **kwargs)
#         ended_at = time.time()
#         elapsed = round(ended_at-started_at, 4)
#         print(f'Функция работала {elapsed} секунд(ы)')
#         return result
#     return surrogate
#
#
# @time_track
# def digits(*args):
#     total = 1
#     for number in args:
#         total *= number ** 5000
#     return len(str(total))
#
# # result = time_track(digits, 3141, 5926, 2718, 2818)
# # time_digits = time_track(digits)
# # result = time_digits(3141, 5926, 2718, 2818)
# # print(result)
#
# # digits = time_track(digits)
# result = digits(3141, 5926, 2718, 2818)
# print(result)
