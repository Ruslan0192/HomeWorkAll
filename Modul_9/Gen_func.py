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
res = lambda x, y: x ** y
print(res(4, 2))


# вызов функции в классе
class Mult:
   def __init__(self, value):
       self.value = value
   def __call__(self, n):
       return self.value * n

res = Mult(value=5)
print(res(n=3))

