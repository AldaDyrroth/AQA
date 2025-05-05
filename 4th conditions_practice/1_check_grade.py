# мой вариант
# def check_grade(score):
#     score = int(score)
#     if 90 <= score <= 100:
#         print(f'Оценка за {score} баллов: Отлично.')
#     elif 75 <= score <= 89:
#         print(f'Оценка за {score} баллов: Хорошо.')
#     elif 50 <= score <= 74:
#         print(f'Оценка за {score} баллов: Удовлетворительно.')
#     elif 0 <= score <= 49:
#         print(f'Оценка за {score} баллов: Неудовлетвортельно.')
#     else:
#         print(f'Совсем дурень? Ты че написал?')
#
# check_grade(77)

def check_grade(score):
    try:
        score = int(score)
    except ValueError:
        return "Ошибка: введите числовое значение."

    text = f'Оценка за {score} баллов:'
    if 90 <= score <= 100:
        text += ' Отлично.'
    elif 75 <= score <= 89:
        text += ' Хорошо.'
    elif 50 <= score <= 74:
        text += ' Удовлетворительно.'
    elif 0 <= score <= 49:
        text += ' Неудовлетворительно.'
    else:
        text = 'Совсем дурень? Ты че написал?'
    return text

# Пример вызова
result = check_grade(-7)
print(result)
