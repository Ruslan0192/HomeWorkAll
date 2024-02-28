print('')
print('пример 1')
x = 38
print('дратути')

if x < 0:
    print('Меньше нуля')
print('до свидание')


print('')
print('пример 2')
a, b = 10, 5

if a > b:
    print('a>b')

if a > b and a > 0:
    print('успех')

if (a > b) and (a > 0 or b < 1000):
    print('успех')

if 5 < b and b < 10:
    print('успех')


# можно сравнивать  - числа, строки, списки и т.п.
print('')
print('пример 3')
if '34' > '123':
    print('успех')

if '123' > '12':
    print('успех')

if [1, 2] > [1, 1]:
    print('успех')


# нельзя сравнивать - разные типы
print('')
print('пример 4')
#if '6' > 5:
#    print('успех')
#
#if [5,6] > 5:
#    print('успех')

#но
if '6' != 5:
    print('успех')

