def group_by_first_letter(strings):
    return {letter: [w for w in strings if w[0] == letter]
          for letter in {word[0] for word in strings}}

strings = ["apple", "apricot", "banana", "blueberry", "cherry"]
print(group_by_first_letter(strings))
# {"a": ["apple", "apricot"], "b": ["banana", "blueberry"], "c": ["cherry"]}