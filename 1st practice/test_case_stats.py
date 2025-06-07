import time

print('Привет! Это снова я, Куа-помощник!')
time.sleep(1.5)
print('На этот раз мы будем считать твою производительность\n'
      'в офомленных тест-кейсах за прошедшую неделю')
time.sleep(1.5)
print('Поехали!')
time.sleep(1.5)
week = {
    "monday": {
        "count": 0,
        "meta": "понедельник"
    },
    "tuesday": {
        "count": 0,
        "meta": "вторник"
    },
    "wednesday": {
        "count": 0,
        "meta": "среда"
    },
    "thursday": {
        "count": 0,
        "meta": "четверг"
    },
    "friday": {
        "count": 0,
        "meta": "пятница"
    }
}
total = 0
print('Сколько тест-кейсов ты составил в этот день недели?')
for day_data in week.values():
    day_data["count"] = int(input(f'{day_data["meta"]}: '))
    total += day_data["count"]
print(f'Всего за предыдушую неделю ты составил {total} тест-кейсов!')
time.sleep(1.5)
average = total / len(week)
if average > 10:
    print(f'Итого в среднем ты составляешь по {average:.2f} тест-кейсов за рабочий день!\n'
          f'Отличный результат!')
else:
    print(f'Печально это все...')
    time.sleep(1.5)
    print(f'C {average:.1f} тест-кейсами за рабочий день...')
    time.sleep(1.5)
    print(f'остается только тапок заминировать...')

