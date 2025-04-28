count = input('Введите любое число: ')
try:
    count = int(count)
except ValueError:
    print('Ой... вы ввели не число!')
else:
    render = count % 10
    print(f'Озон был рад твоему {render}см монстру')