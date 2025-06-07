def calculator():
    def sloj(a,b):
        return round(a + b,1)
    def vych(a,b):
        return round(a - b,1)
    def umnj(a, b):
        return round(a * b,1)
    def deln(a,b):
        return round(a / b,1)

    def chislo(g):
        arg = 0
        while arg == 0:
            try:
                g = float(g)
            except ValueError:
                g = input('Ой... вы ввели не число!\n')
            else:
                arg = 1
        return g

    a = chislo(input('Вводи число, мамонт: '))

    b = chislo(input('И второе: '))

    action = input('Выбирай операцию (пластической нет)(+, -, *, /): ')
    if action == '+':
        print('Результат: ', sloj(a,b))
    elif action == '-':
        print('Результат: ', vych(a, b))
    elif action == '*':
        print('Результат: ', umnj(a, b))
    elif action == '/':
        print('Результат: ', deln(a, b))
    else:
        print('Ты чо, дурак бл????')
while True:
    calculator()