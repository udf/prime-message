import sys

def eratosthenes():
    # Modified version from the second page:
    # archive.oreilly.com/pub/a/python/excerpt/pythonckbk_chap1/index1.html
    q = 3
    D = {}
    yield 2
    while True:
        p = D.pop(q, None)
        # Check 'if p' instead 'if p is None', which is around 15% faster.
        if p:
            # Used to be 'x = p + q', and then 'or x even' in the loop,
            # implemented as 'or not (x&1)'.
            #
            # We know that q is always odd, and p is q*q (where q is odd prime)
            # Multiplying an odd number by any other (or even itself) is always
            # odd. Adding two odds together is always even, so we always need
            # to add p again, or simply add 2p. This is around 30% faster.
            p2 = p * 2
            x = p2 + q
            while x in D:
                x += p2
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
