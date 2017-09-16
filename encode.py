import sys

def eratosthenes():
    # Slightly modified version from:
    # archive.oreilly.com/pub/a/python/excerpt/pythonckbk_chap1/index1.html
    # Check 'if p' instead 'if p is None', which is around 15% faster.
    D = {}
    q = 2
    while True:
        p = D.pop(q, None)
        if p:
            x = p + q
            while x in D:
                x += p
            D[x] = p
        else:
            yield q
            D[q*q] = q
        q += 1

gen = eratosthenes()
product = 1
msg = "".join(sys.argv[1:])
length = len(msg)
for i, char in enumerate(msg):
    char_ord = ord(char)
    while True:
        n = next(gen)
        if (n >> 1) & 0b11111111 == char_ord:
            print("{}/{} = {}".format(i+1, length, n), end="\r")
            product *= n
            break

print()
print(product)
