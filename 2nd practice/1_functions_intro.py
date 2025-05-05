def greet_user(name):
    print(f'Привет, {name}! Добро пожаловать в мир Python!')

def calculate_sum(a, b):
    return a + b

def chislo(a):
    arg = 0
    while arg == 0:
        try:
            a = int(a)
        except ValueError:
            a = input('Ой... вы ввели не число!\n')
        else:
            arg = 1
    return a

man = greet_user(input('Введите ваше имя: ').title())

m = chislo(input(f'Введите рандомные числа и я их сложу :)\n'))

n = chislo(input(f'А теперь второе :)\n'))

print(calculate_sum(m,n))