TempF = input('Введите темературу в градусах Фаренгейта ')
try:
    TempF = int(TempF)
except ValueError:
    print('Ой... вы ввели не число!')
else:
    TempC = round((TempF - 32) * 5 / 9, 1)
    print(f'Поздравляем, ваша температура составляет {TempC} градусов цельсия!')




