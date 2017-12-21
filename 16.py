
def swap(s, i1, i2):
    ll = [c for c in s]
    tmp = ll[i1]
    ll[i1] = ll[i2]
    ll[i2] = tmp
    s = "".join(ll)
    return s

f = open("16").read().strip().split(',')

assert f[0] == "s11"
assert f[-1] == "x12/7"

orig = "abcdefghijklmnop"
l = "abcdefghijklmnop"

dances = 1000000000 % 48

for i in range(dances):

    for x in f:
        assert len(l) == 16
        for char in l:
            assert char in orig
        if x[0] == "s":
            s = int(x[1:])
            l = l[-s:] + l[:-s]
        elif x[0] == "x":
            xx = x[1:].split('/')
            assert len(xx) == 2
            l = swap(l, int(xx[0]), int(xx[1]))
        elif x[0] == "p":
            xx = x[1:].split('/')
            assert len(xx) == 2
            assert len(xx[0]) == len(xx[1]) == 1
            assert xx[0] in l
            assert xx[1] in l
            l = swap(l, l.index(xx[0]), l.index(xx[1]))
        else:
            assert False

    if i % dances / 100 == 0:
        print float(i) / float(dances)

    if l == orig:
        print i
        break

print l