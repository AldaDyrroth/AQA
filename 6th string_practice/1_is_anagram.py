def is_anagram(s1, s2):
    word1 = []
    word2 = []
    for i in range(len(s1)):
        word1.append(s1[i])
        word2.append(s2[i])
    print(word1,word2)
    if set(word1) == set(word2):
        return True
    else:
        return False
# print(is_anagram("listen", "silent"))
print(is_anagram("кабан", "банка"))  # True
