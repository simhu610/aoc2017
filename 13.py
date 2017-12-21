
f = open("13").readlines()

x = {}

for line in f:
    ab = line.split()
    a = int(ab[0].replace(':', ''))
    b = int(ab[1])
    x[a] = {'range': b}

delay = 0

while True:

    for l in x:
        x[l]['pos'] = 0
        x[l]['v'] = 1

    layer = -1
    severity = 0
    d = delay

    while layer < max(x.keys()):
        if d == 0:
            layer += 1
            if layer in x and x[layer]['pos'] == 0:
                severity += layer * x[layer]['range']
        else:
            d -= 1
        for l in x:
            x[l]['pos'] += x[l]['v']
            if x[l]['pos'] == 0 or x[l]['pos'] == x[l]['range'] - 1:
                x[l]['v'] *= -1

    print delay, severity

    if severity == 0:
        break
    else:
        delay += 2