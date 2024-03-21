# Генератор функций
def create_operation(operand):
    if operand == '+':
        def operation(x, y):
            return x + y
        return operation
    elif operand == '-':
        def operation(x, y):
            return x - y
        return operation
    elif operand == '*':
        def operation(x, y):
            return x * y
        return operation
    elif operand == '/':
        def operation(x, y):
            return x / y
        return operation
    else:
        print(f'неправильный операнд: "{operand}"')


try:
    my_func_add = create_operation('/')
except:
    print('Функция не определена')
try:
    print(my_func_add(2,0))
except:
    print('деление на ноль')

# лямбда функция
list1 = [1, 2, 5, 32, 2]
y = 2
res = map(lambda x: x * y, list1)
print(list(res))


# вызов функции в классе
class Mult:
   def __init__(self, value):
       self.value = value
   def __call__(self, n):
       return self.value * n

list1 = [1, 2, 5, 32, 2]
five = Mult(value=5)
res = map(five, list1)
print(list(res))

