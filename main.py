import hashlib, random


def prexor(a):
    a = str(a)
    l = []
    for i in a:
        l.append(ord(i))



def xor(a, b):
    res = []
    l = len(b)
    n = 0
    for i in a:
        x = i ^ b[n]
        res.append(x)
        n += 1
        if n == l:
            n = 0
    return res


def readypassword(password, passlen):
    password = str(password)
    l = ''
    n = 1
    while True:
        for i in password:
            l += hashlib.md5((i + password * n).encode()).hexdigest()
        if len(l) > passlen:
            l = xor(l.encode(), xor(password.encode(), hashlib.md5(password.encode()).hexdigest().encode()))
            return l
        n += 1


def normalizer(x):
    res = ''
    for i in x:
        res += chr(i)
    return res


def shiftr(x):
    return x[-1:] + x[:-1]


def shiftl(x):
    return x[1:] + x[:1]


def ranger(x):
    if x > 1114111:
        return 1114111
    elif x < 0:
        return 0
    else:
        return x


def encrypt(text, password):
    additional_len = len(password) * 2
    maxchar, minchar = max(text.encode()), min(text.encode())
    changedtext = []
    for i in range(additional_len):
        changedtext.append(random.randint(ranger(minchar - 100), ranger(maxchar + 100)))
    changedtext += list(text.encode())
    for i in range(additional_len):
        changedtext.append(random.randint(ranger(minchar - 100), ranger(maxchar + 100)))
    repass = readypassword(password, len(changedtext))
    for i in range(len(repass)):
        changedtext = xor(changedtext, repass)
        changedtext = shiftr(changedtext)
    return changedtext


def decrypt(etext, password):
    additional_len = len(password) * 2
    repass = readypassword(password, len(etext))
    for i in range(len(repass)):
        etext = shiftl(etext)
        etext = xor(etext, repass)
    etext = etext[additional_len: additional_len*-1]
    return etext

x = encrypt('hello','hello')
print(normalizer(x))
print(normalizer(decrypt(x, 'hello')))
