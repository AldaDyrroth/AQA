def greet_user(name):
    print(f'Привет, {name}! Добро пожаловать в мир Python!')

def calculate_sum(a, b):
    print(a + b)

man = input('Введите ваше имя: ').title()
greet_user(man)

m = input(f'Введите рандомные числа и я их сложу :)\n')
arg = 0
while arg == 0:
    try:
        m = int(m)
    except ValueError:
        m = input('Ой... вы ввели не число!')
    else:
        arg = 1

n = input(f'А теперь второе :)\n')
arg = 0
while arg == 0:
    try:
        n = int(n)
    except ValueError:
        n = input('Ой... вы ввели не число!')
    else:
        arg = 1

calculate_sum(m,n)