
def ascii(l):
    if l == ',':
        return 44
    else:
        return int(l) + 48

assert ascii(',') == 44
assert ascii('0') == 48
assert ascii('9') == 57


def string_to_lengths(s):
    return [ord(l) for l in s] + [17, 31, 73, 47, 23]

assert string_to_lengths("1,2,3") == [49,44,50,44,51,17,31,73,47,23]


def read_input():
    return open("10").read().strip()

assert read_input() == "34,88,2,222,254,93,150,0,199,255,39,32,137,136,1,167"


def shuffle(lengths, rounds):
    x = range(256)
    i = 0
    step = 0

    for _ in range(rounds):
        for l in lengths:
            assert 0 <= i < 256
            assert 0 <= l < 256
            if i + l <= 256:
                x = x[:i] + list(reversed(x[i:i+l])) + x[i+l:]
            else:
                to_reverse = x[i:] + x[:(i + l) % 256]
                y = list(reversed(to_reverse))
                x = y[256 - (i + l):] + x[(i + l) % 256:i] + y[:256 - (i + l)]
            i += l
            i += step
            i %= 256
            step += 1
    assert step == rounds * len(lengths)
    return x

x1 = shuffle([int(l) for l in read_input().strip().split(',')], 1)
assert x1[0] * x1[1] == 54675


def block_xor(block):
    import operator
    return reduce(operator.xor, block)

assert block_xor([65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]) == 64


def get_blocks(sparse):
    return [sparse[16 * block:16 * (block + 1)] for block in range(16)]

b1 = get_blocks(range(256))
assert len(b1) == 16
assert all([len(b2) == 16 for b2 in b1])
b3 = []
for b4 in b1:
    b3 = b3 + b4
assert b3 == range(256)


def densify(sparse):
    return [block_xor(block) for block in get_blocks(sparse)]

d1 = densify(range(256))
assert len(d1) == 16
assert all([0 <= d2 < 256 for d2 in d1])


def hexify(dense):
    return "".join(["{:02x}".format(d) for d in dense])

assert hexify([64, 7, 255]) == "4007ff"


def knot_hash(input_string):
    lengths = string_to_lengths(input_string)
    sparse = shuffle(lengths, 64)
    assert sorted(sparse) == range(256)
    dense = densify(sparse)
    return hexify(dense)

assert len(knot_hash("42,42")) == 32
print knot_hash(""), "a2582a3a0e66e6e86e3812dcb672a272"
print knot_hash("1,2,3"), "3efbe78a8d82f29979031a4aa0b16a9d"
print knot_hash("1,2,4"), "63960835bcdc130f0b66d7ff4f6a5a8e"
assert knot_hash("") == "a2582a3a0e66e6e86e3812dcb672a272"
# assert knot_hash("AoC 2017") == "33efeb34ea91902bb2f59c9920caa6cd"
assert knot_hash("1,2,3") == "3efbe78a8d82f29979031a4aa0b16a9d"
assert knot_hash("1,2,4") == "63960835bcdc130f0b66d7ff4f6a5a8e"

print knot_hash(read_input())
