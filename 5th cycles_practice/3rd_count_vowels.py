def count_vowels(string):
    result = 0
    for i in range(len(string)):
        if string[i] in 'eyuoai':
            result += 1
    print(f'Количество гласных в строке "{string}": {result}')

count_vowels("Hello World")