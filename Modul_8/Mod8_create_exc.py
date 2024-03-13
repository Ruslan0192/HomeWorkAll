class Exc_on_int (Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f'значение {self.value} не целое число'

class Exc_min (Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f'Результат {self.value} меньше'

def control(value):
    value_int = int(value)
    if value == value_int:
        return True
    return False

def div():
    try:
        a = float(input('введите делимое '))
        if control(a) == False:
            raise Exc_on_int('делимого')

        b = float(input('введите делитель '))
        if control(b) == False:
            raise Exc_on_int('делителя')

        result = a/b
        if control(result) == False:
            raise Exc_on_int(f'результата ({result})')
        if result < min_value:
            raise Exc_min(result)
        return f'результат: {result}'
    except Exc_on_int as info_error:
        return info_error
    except Exc_min as info_error:
        return f'{info_error} {min_value}'
    except ZeroDivisionError:
        return 'Деление на ноль'
    except ValueError:
        return f'значение не является числом'
    else:
        return 'неопознанная ошибка'

min_value = 10
print(div())


