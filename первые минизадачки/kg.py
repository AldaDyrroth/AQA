gramm = input('Введите массу вещества в граммах: ')
try:
    gramm = int(gramm)
except ValueError:
    print('Ой... вы ввели не число!')
else:
    kg = gramm // 1000
    print(f'Крутотень! у тебя целых {kg} килограммов говна!')