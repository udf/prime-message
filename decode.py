import sys

def factors(n):
    """Yields all the prime factors for n"""
    if n < 2:
        return
    if n % 2 == 0:
        yield 2
        n //= 2
        if n == 1:
            return
    i = 3
    limit = int(n**0.5)+1
    while i < limit:
        m, r = divmod(n, i)
        if r == 0:
            yield i
            n = m
            limit = int(n**0.5)+1
        i += 2
    yield n


def decode(n):
    """Decodes a prime-based hidden message"""
    return ''.join(chr(f >> 1 & 0xFF) for f in factors(n))


if __name__ == '__main__':
    for arg in sys.argv[1:]:
        print(decode(int(arg)))
