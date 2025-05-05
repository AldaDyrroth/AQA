def longest_word(s):
    formatted_text = ''
    for i in range(len(s)):
        if s[i] not in '!@#$%^&*()-_+=|{}[]:;\"\'<>,.?/':
            formatted_text += s[i]
    words = formatted_text.split()
    print(words)
    result = ''
    for j in range(len(words)):
        if len(words[j]) > len(result):
            result = words[j]
    print(result)

longest_word('Палиндромы могут быть как простыми словами, так и сложными фразами и даже стихами. Многие из них создавались известными авторами и поэтами, а также используются в литературных и интеллектуальных играх')