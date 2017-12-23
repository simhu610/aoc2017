primes = []
vals_tested = 0
h = 0
b = 81
b *= 100
b += 100000
c = b
c += 17000
while b <= c:
    f = 1
    d = 2
    while d < b:
        if b % d == 0:
            f = 0
            break
        d += 1
    if f == 0:
        h += 1
    else:
        primes.append(b)
    b += 17
    vals_tested += 1
print h

print primes
print vals_tested, len(primes)