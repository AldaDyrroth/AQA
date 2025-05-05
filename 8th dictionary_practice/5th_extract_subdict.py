def extract_subdict(my_dict, keys):
    return {x: my_dict.get(x, 0) for x in set(my_dict) if x in keys}

my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
keys = ["a", "c"]
print(extract_subdict(my_dict, keys))  # {"a": 1, "c": 3}