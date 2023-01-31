def commonWords(str1, str2):
    s1 = set(str1)
    s2 = set(str2)
    common = list(s1.intersection(s2))
    return common
def removeCommonWords(str1, str2):
    sentence1 = list(str1.split())
    sentence2 = list(str2.split())
    commonlist = commonWords(sentence1,
                             sentence2)
 
    word = 0
    for i in range(len(sentence1)):
        if sentence1[word] in commonlist:
            sentence1.pop(word)
            word = word - 1
        word += 1
 
    word = 0
    for i in range(len(sentence2)):
        if sentence2[word] in commonlist:
            sentence2.pop(word)
            word = word-1
        word += 1
    print(*sentence1)
    print(*sentence2)
S1 = input("enter string1")
S2 = input("enter string2") 
removeCommonWords(S1, S2)
