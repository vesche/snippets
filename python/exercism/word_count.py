import re

def word_count(s):
    d = {}
    s = re.sub('[^0-9a-zA-Z]+', ' ', s.lower()).split()
    for word in s:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d
