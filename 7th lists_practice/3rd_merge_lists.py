def merge_lists(list1, list2):
    result = list(set(list1 + list2))
    return result

print(merge_lists([1, 2, 3], [3, 4, 5]))