import sys

def eratosthenes():
    # Slightly modified version from the second page:
    # archive.oreilly.com/pub/a/python/excerpt/pythonckbk_chap1/index1.html
    # Check 'if p' instead 'if p is None', which is around 15% faster.
    q = 3
    D = {}
    yield 2
    while True:
        p = D.pop(q, None)
        if p:
            x = p + q
            while x in D or not (x&1):
                x += p
            D[x] = p
        else:
            yield q
            D[q*q] = q
        q += 2

def encode(msg):
    gen = eratosthenes()
    product = 1
    for c in msg:
        target = ord(c)
        while True:
            n = next(gen)
            if (n >> 1) & 0xff == target:
                product *= n
                break
    return product


if __name__ == '__main__':
    print(encode(' '.join(sys.argv[1:])))
