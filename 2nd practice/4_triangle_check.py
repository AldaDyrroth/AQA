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

def chislo(a):
    arg = 0
    while arg == 0:
        try:
            a = int(a)
        except ValueError:
            a = input('Ой... вы ввели не число!\n')
        else:
            arg = 1
    return a

Side1 = chislo(input('Гони сторону треугольника: '))

Side2 = chislo(input('И вторую давай сюда: '))

Side3 = chislo(input('Все до гроша: '))

check_triangle(Side1, Side2, Side3)

