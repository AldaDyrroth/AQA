def sum_numbers(n):
    total = 0
    for i in range(n+1): total += i
    print(f'Сумма чисел от 1 до {n}: {total}')

sum_numbers(7)
