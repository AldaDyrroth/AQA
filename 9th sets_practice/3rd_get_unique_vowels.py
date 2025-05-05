def get_unique_vowels(s):
    return {x for x in set(s) if x in 'eyuoai'}

print(get_unique_vowels("Eve eases a sea"))  # {'e', 'o'}