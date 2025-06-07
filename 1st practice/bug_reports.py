import time

bug = [
    'Ошибка 1 - High',
    'Ошибка 2 - Low',
    'Ошибка 3 - Medium',
    'Ошибка 4 - High',
    'Ошибка 5 - Medium'
]
print(f'Приветствую! Вам представлен актуальный список багов')
time.sleep(1)
for i in bug:
    print(i)
time.sleep(1)
priority_order = {'High': 0, 'Medium': 1, 'Low': 2}
arg1 = 0
while arg1 == 0:
    rqst = input('Что бы вы хотели сделать?\n'
                 '1)Добавить баг\n'
                 '2)Удалить баг с низким приоритетом\n'
                 '3)Отсортировать список багов\n'
                 '4)Завершить сессию\n')
    if rqst == '1':
        new_bug = input('Баг с каким приоритетом вы хотите добавить?\n'
                        '1)High (высокий)\n'
                        '2)Medium (средний)\n'
                        '3)Low (низкий)\n')
        arg = 0
        while arg == 0:
            try:
                new_bug in ('1','2','3')
            except ValueError:
                new_bug = input(f'Что-то не так, давай попробуем еще раз:\n')
            else:
                arg += 1
                if new_bug == '1':
                    bug.append(f'Ошибка {len(bug)+1} - High')
                elif new_bug == '2':
                    bug.append(f'Ошибка {len(bug)+1} - Medium')
                elif new_bug == '3':
                    bug.append(f'Ошибка {len(bug)+1} - Low')
                else:
                    print('Что-то здесь не так...')
                    time.sleep(1)
        for i in bug:
            print(i)
    elif rqst == '2':
        arg = 0
        for i in bug:
            if 'Low' in i and arg == 0:
                bug.remove(i)
                arg += 1
        for i in bug:
            print(i)
    elif rqst == '3':
        # Функция для извлечения приоритета из строки
        def get_priority(item):
            # Разбиваем строку по дефису и пробелам, берём последний элемент (приоритет)
            priority = item.split('-')[-1].strip()
            return priority_order.get(priority, 99)  # если приоритет не найден, ставим большой номер
        # Сортируем список по приоритету
        bug_sorted = sorted(bug, key=get_priority)
        # Выводим результат
        for b in bug_sorted:
            print(b)
        # print('Функция находится в разработке!')
    else:
        arg1 += 1
        print('Сессия завершена! Еще увидимся!')


# bug.append()
# bug.remove()
# bug.sort    time.sleep(1)

