import sys

def decode(n):
    factors = []

    for i in range(3, n, 2):
        while n % i == 0:
            n //= i
            factors.append(i)
        if n == 1:
            break

    return "".join(chr(f >> 1 & 0xFF) for f in factors)
    

for arg in sys.argv[1:]:
    print(decode(int(arg)))
