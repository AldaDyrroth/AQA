name = input('Привет, меня зовут Куа-помощник! Как тебя зовут?\n')
name = name.title()
pro = input(f'{name}, какова твоя профессия?\n')
arg = 0
while arg == 0:
    try:
        pro = int(pro)
    except ValueError:
        print(f'Итак, тебя зовут {name} и твоя профессия - {pro}!')
        arg =+ 1
    else:
        pro = input('Какая странная у тебя профессия... \nможет, она все таки по другому называется?\n')
time = input('И сколько же ты уже работаешь на этой должности (в годах)?\n')
arg = 0
while arg == 0:
    try:
        time = int(time)
    except ValueError:
        time = input('Я не понимаю такие числа :(\n')
    else:
        print(f'Целых {time} лет!')
        arg =+ 1
ans = int(input('А ты знаешь, что такое переменная?\n'
            '1)именованная ячейка памяти для хранения данных\n'
            '2)вид погоды, характеризующаяся резкими сменами температуры и осадков\n'
            '3)это промежуток между уроками в школе\n'
            'В качестве ответа укажи номер варианта, который считаешь правильным :)\n'))
while ans != '1':
    ans = input('Несовсем так, попробуй еще раз :)\n')

print('Wow! Да передо мной настоящий Senior AQA!\n'
      'Еще увидимся, было приятно поболтать с тобой! :3')

