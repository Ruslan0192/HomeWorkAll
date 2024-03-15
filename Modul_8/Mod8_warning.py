import warnings
def div(a,b):
    if b < 0.01:
        warnings.warn('делитель близок к нулю', category=UserWarning)
    a = a/b
    print(f'делитель {b} результат {a}')
    b = b/10
    return b

a = 1000
b = 100

# warnings.simplefilter('always')
# warnings.simplefilter('ignore')
warnings.simplefilter('error')
# warnings.simplefilter('once')

for _ in range(10):
    try:
        b = div(a,b)
    except UserWarning:
        print('Исключение: делитель близок к нулю, пропускаю')