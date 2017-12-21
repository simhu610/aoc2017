
f = open("13").readlines()

x = {}

for line in f:
    ab = line.split()
    a = int(ab[0].replace(':', ''))
    b = int(ab[1])
    x[a] = {'range': b}

delay = 0

while True:
    fail = False
    for l in x:
        # print delay, l, x[l]['range']
        # print delay + l, ((x[l]['range'] - 1) * 2)
        if (delay + l) % ((x[l]['range'] - 1) * 2) == 0:
            # print "fail", delay, l
            fail = True
            break
    if not fail:
        print "success", delay
        break
    delay += 2