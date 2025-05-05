def is_even(number):
    if number % 2 == 0:
        return f'Число {number} является чётным'
    else:
        return f'Число {number} является нечётным'

print(is_even(1))