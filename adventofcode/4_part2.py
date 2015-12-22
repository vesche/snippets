import hashlib

secret = "ckczppom"
n = 1

def md5hash(string):
    m = hashlib.md5()
    m.update(string)
    return m.hexdigest()[0:6]

while 1:
    if md5hash(secret + str(n)) == '000000':
        print n
        break
    n += 1
