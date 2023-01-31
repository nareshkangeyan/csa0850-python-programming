def last_word_length(s):
    words = s.strip().split(" ")
    return len(words[-1])

s = input("enter the word :")
print(last_word_length(s))
