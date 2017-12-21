def knot_hash(k):
    return "a5a5a5a5a5a5a5a5a5a5a5a5a5a5a5a5"

key = "vbqugkhl"
used = 0

for i in range(128):
    k = "{}-{}".format(key, i)
    h = knot_hash(k)
    s = "{0:b}".format(int(h, 16))
    n = [int(b) for b in s]
    used += sum(n)

print used

nn = []

for i in range(1000000):
    s = "{0:b}".format(i)
    n = sum([int(b) for b in s])
    nn.append(n)

import matplotlib.pyplot as plt
plt.plot(nn)
plt.show()