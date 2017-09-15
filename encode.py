import sys

def eratosthenes():
    D = {}
    q = 2  
    while 1:
        if q not in D:
            yield q
            D[q*q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p+q,[]).append(p)
            del D[q]
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
            print("{}/{} = {}".format(i, length, n), end="\r")
            product *= n
            break

print(product)