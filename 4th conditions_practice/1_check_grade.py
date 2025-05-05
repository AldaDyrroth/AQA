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

    if 90 <= score <= 100:
        return f'Оценка за {score} баллов: Отлично.'
    elif 75 <= score <= 89:
        return f'Оценка за {score} баллов: Хорошо.'
    elif 50 <= score <= 74:
        return f'Оценка за {score} баллов: Удовлетворительно.'
    elif 0 <= score <= 49:
        return f'Оценка за {score} баллов: Неудовлетворительно.'
    else:
        return 'Совсем дурень? Ты че написал?'

# Пример вызова
result = check_grade(77)
print(result)
