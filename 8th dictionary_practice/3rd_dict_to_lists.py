def dict_to_lists(my_dict):
    return (list(my_dict.keys()), list(my_dict.values()))

my_dict = {"a": 1, "b": 2, "c": 3}
print(dict_to_lists(my_dict))  # (["a", "b", "c"], [1, 2, 3])

