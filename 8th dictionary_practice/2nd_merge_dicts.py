def merge_dicts(dict1, dict2):

    return {
    key: dict1.get(key, 0) + dict2.get(key, 0)
    for key in set(dict1) | set(dict2)
}

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
print(merge_dicts(dict1, dict2))  # {"a": 1, "b": 5, "c": 4}