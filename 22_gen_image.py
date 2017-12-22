import matplotlib.pyplot as plt

m = [row.strip() for row in open("22_output_test.txt").readlines()]

import random

def get_r():
    return random.randint(0, 255 - 50 - 50)

r1 = get_r()
r2 = get_r()
r3 = get_r()
r4 = get_r()

f = {'.': r1,
     ':': r1,
     'W': r2,
     'w': r2,
     'F': r3,
     'f': r3,
     '#': r4,
     'X': r4}

def ff(c, x, y):
    if c in f:
        return f[c] + random.randint(0, x / 7) + random.randint(0, y / 7)
    else:
        assert False, c

m2 = [[ff(c, x, y) for x, c in enumerate(row)] for y, row in enumerate(m)]

print m2

plt.imshow(m2[:-1])
plt.show()