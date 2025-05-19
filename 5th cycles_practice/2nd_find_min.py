def find_min(numbers):
    result = 0
    for i in range(len(numbers)):
        if numbers[i] < numbers[i-1]:
            result = numbers[i]
    print(f'Минимальное число в списке {numbers}:  {result}')

find_min([3, 10, 4, 2, 5])