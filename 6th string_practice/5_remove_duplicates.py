def remove_duplicates(s):
    formatted_word = ''
    for i in range(len(s)):
        if s[i] not in formatted_word:
            formatted_word += s[i]
    return formatted_word

print(remove_duplicates("sdhklfgjjdksgsdklgdghklshfgkjlgs"))