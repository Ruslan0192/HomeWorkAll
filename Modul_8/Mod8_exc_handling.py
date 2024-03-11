def string_to_int(s): # обработка ValueError
    try:
        return int(s)
    except ValueError:
        return f'{s} не целое число'
    else:
        return 'неопознанная ошибка'

def read_file(filename): # обработка FileNotFoundError, IOError
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f'файл {filename} не найден'
    except IOError:
        return f'Ошибка ввода/вывода файла {filename}'
    except Exception:
        return 'неопознанная ошибка'

def divide_numbers(a, b): # обработка ZeroDivisionError, TypeError
    try:
        return a / b
    except ZeroDivisionError:
        return 'Деление на ноль'
    except TypeError:
        return f'{a} и/или {b} не числа'

def access_list_element(lst, index): # обработка IndexError, TypeError
    try:
        return lst[index]
    except IndexError:
        return f'{index} вне диапазона списка'
    except TypeError:
        return 'Индекс не целое число'

print(string_to_int(23))
print(string_to_int('ert'))
print('*'*20)

file_name = 'test.txt'
print(read_file(file_name))
file_name = 'test1.txt'
print(read_file(file_name))
print('*'*20)

print(divide_numbers(9,3))
print(divide_numbers(9,0))
print(divide_numbers(9,'r'))
print('*'*20)

test_list = ['w', 'e']
print(access_list_element(test_list,0))
print(access_list_element(test_list,3))
print(access_list_element(test_list,'0'))