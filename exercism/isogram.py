def is_isogram(word):
    word = filter(str.isalnum, word.lower())
    return len(list(word)) == len(set(word))
