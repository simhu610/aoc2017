h = 0
b = 81
c = b
b *= 100
b += 100000
c = b
c += 17000
g = -1
while g != 0:
    f = 1
    d = 2
    g = -1
    while g != 0:
        e = 2
        g = -1
        while g != 0:
            g = d
            g *= e
            g -= b
            if g == 0:
                f = 0
            e += 1
            g = e
            g -= b
        d += 1
        g = d
        g -= b
        print d
    if f == 0:
        h += 1
    g = b
    g -= c
    b += 17
    print b
print h