def hey(s):
    s = ''.join(s.split())
    if not s:
        return 'Fine. Be that way!'
    elif s.isupper():
        return 'Whoa, chill out!'
    elif s.endswith('?'):
        return 'Sure.'
    else:
        return 'Whatever.'
