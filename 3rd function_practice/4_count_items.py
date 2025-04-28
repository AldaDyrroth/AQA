def count_items(*args):

    result = len(args)
    print(f'Количество переданных элементов: {result}.')

count_items(1,2,3,4,5,"gog")