def check_number(number):
    text = ''
    if number >= 0:
        text = f'Число {number} положительное'
        if number % 2 == 0:
            text += ' и четное'
    else:
        text = f'Число {number} отрицательное'
    text += '.'
    return text

print(check_number(-7))