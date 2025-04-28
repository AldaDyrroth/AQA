def calculator():
    def sloj(a,b):
        return round(a + b,1)
    def vych(a,b):
        return round(a - b,1)
    def umnj(a, b):
        return round(a * b,1)
    def deln(a,b):
        return round(a / b,1)
    a = input('Вводи число, мамонт: ')
    arg = 0
    while arg == 0:
        try:
            a = int(a)
        except ValueError:
            a = input('Мудак, я сказал число!')
        else:
            arg = 1
    b = input('И второе: ')
    arg = 0
    while arg == 0:
        try:
            b = int(b)
        except ValueError:
            b = input('Мудак, я сказал число!')
        else:
            arg = 1
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