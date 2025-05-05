def is_unique(s):
    result = 0
    formatted_word = ''
    for i in range(len(s)):
        if s[i] not in formatted_word:
            formatted_word += s[i]
        else:
            result =+ 1
    if result == 0:
        return True
    else:
        return False

print(is_unique("qwertyuiopq"))