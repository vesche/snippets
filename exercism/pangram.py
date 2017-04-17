def is_pangram(word):
    word = filter(str.isalpha, word.lower())
    return len(set(word)) == 26
