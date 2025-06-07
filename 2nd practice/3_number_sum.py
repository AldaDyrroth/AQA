n = input('Погнали считать! Вбивай число: ')
arg = 0
while arg == 0:
    try:
         n = int(n)
    except ValueError:
        n = input('Ой... вы ввели не число!')
    else:
        arg = 1
total = 0
for i in range(n):
    print(i+1, end=' ')
    total += int(i)+1
print(f'\nСумма чиссссел: {total}')