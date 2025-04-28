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
tool = input("Введите ваш любимый инструмент для тестирования:\n")
arg = False
while arg == False:
    if not tool:
         tool = input("Инструмент не указан. Попробуйте снова!\n")
    else:
        arg = True
        print(f"Ваш любимый инструмент: {tool}. Отличный выбор!")