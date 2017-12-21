import numpy as np

r = open("21").readlines()
# r = ["../.# => ##./#../...", ".#./..#/### => #..#/..../..../#..#"]

rules = {}

for line in r:
    r1 = line.strip().split(' => ')
    ins = r1[0]
    outs = r1[1]
    rules[ins] = outs

print rules

def get_arr(s):
    return np.array([np.array([c for c in row]) for row in s.split('/')])

def get_string(m):
    return '/'.join([''.join(r) for r in m])

def transform(x):
    for num_rots in range(4):
        rotated = np.rot90(x, num_rots)
        str = get_string(rotated)
        if str in rules:
            return get_arr(rules[str])
        for flip_axis in [0, 1]:
            str = get_string(np.flip(rotated, flip_axis))
            if str in rules:
                return get_arr(rules[str])
    assert False, "no rule (of {}) found for: {}".format(len(rules), str)

image = ".#./..#/###"

assert get_string(get_arr(image)) == image

image = get_arr(image)
print image

for i in range(18):
    print i
    size = len(image)
    mod = 2 if size % 2 == 0 else 3
    new_image = np.array([]).reshape(0, size / mod * (mod + 1))
    sub_range = range(size / mod)
    for row in sub_range:
        image_row = image[row * mod:(row + 1) * mod]
        new_row = np.array([]).reshape(mod + 1, 0)
        for col in sub_range:
            sub_square = image_row[:,col * mod:(col + 1) * mod]
            transformed = transform(sub_square)
            new_row = np.append(new_row, transformed, axis=1)
        new_image = np.append(new_image, new_row, axis=0)
    image = new_image
    print image

print sum([sum([c == '#' for c in row]) for row in image])