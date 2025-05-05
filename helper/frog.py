def IntVal(num):
    arg = 0
    while arg == 0:
        try:
            num = int(num)
        except ValueError:
            num = input('Ой... вы ввели не число!')
        else:
            arg = 1
            return num

print(type(len('frog')))

print(range(4))