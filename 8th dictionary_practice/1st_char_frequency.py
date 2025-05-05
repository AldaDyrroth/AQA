def char_frequency(s):
    return {x: s.count(x) for x in set(s)}

print(char_frequency("hello"))  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}