
steps = 370
pos = 0

buf = [0]
N = 50*1000*1000
L = 1

for i in range(1, N):
    # pos = (pos + steps) % len(buf)
    pos = (pos + steps) % L
    L += 1
    if pos == 0:
        print i
    # buf.insert(pos + 1, i)
    pos += 1

# assert len(buf) == N
#
# print buf