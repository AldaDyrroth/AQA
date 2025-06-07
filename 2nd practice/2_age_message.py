import time
from datetime import date, datetime
import helper

print('Привет! На связи Куа-помощник! \nСегодня будем покупать алко на день рождения!')
time.sleep(1.5)
year = input('Введи год своего рождения\n')
arg = 0
while arg == 0:
    try:
         year = int(year)
    except ValueError:
        year = input('Ой... вы ввели не число!')
    else:
        arg = 1
CurYear = date.today().year
age = CurYear - year
print(f'Скорее всего вам сейчас {age} лет (или год/года)')
if age < 18:
    print('Вы еще молоды, учеба — ваш путь!')
elif age > 65:
    print('Пора наслаждаться заслуженным отдыхом!')
else:
    print('Отличный возраст для карьерного роста!')