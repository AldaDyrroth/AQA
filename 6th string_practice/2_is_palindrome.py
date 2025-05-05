import math

def is_palindrome(s):
    formatted_word = ''
    for i in range(len(s)):
        if s[i] not in ' !@#$%^&*()-_+=|{}[]:;\"\'<>,.?/':
            formatted_word += s[i]
    formatted_word = formatted_word.lower()
    print(formatted_word)
    formatted_word2 = formatted_word[::-1]
    if formatted_word == formatted_word2:
        return True
    else:
        return False




print(is_palindrome('И черви, и лилии в речи'))

