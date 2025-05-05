def check_triangle(a, b, c):
    assert a + b > c, "Мудак, у тебя не треугольник, а дилдо получился!"
    assert a + c > b, "Мудак, у тебя не треугольник, а дилдо получился!"
    assert c + b > a, "Мудак, у тебя не треугольник, а дилдо получился!"
    if a == b == c:
        print('Мавроди тобой гордится! (правильная пирамида/треугольник)!')
    elif a == b or a == c or b ==c:
        print('Равнобедренный, как училка!')
    else:
        print('Слава Богу, это хотя бы треугольник, а не дилдо!')
Side1 = input('Гони сторону треугольника: ')
arg = 0
while arg == 0:
    try:
        Side1 = int(Side1)
    except ValueError:
        Side1 = input('Мудак, я сказал число!')
    else:
        arg = 1
Side2 = input('И вторую давай сюда: ')
arg = 0
while arg == 0:
    try:
         Side2 = int(Side2)
    except ValueError:
        Side2 = input('Мудак, я сказал число!')
    else:
        arg = 1
Side3 = input('Все до гроша: ')
arg = 0
while arg == 0:
    try:
         Side3 = int(Side3)
    except ValueError:
        Side3 = input('Мудак, я сказал число!')
    else:
        arg = 1
check_triangle(Side1, Side2, Side3)

