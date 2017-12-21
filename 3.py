import numpy

C = 100

def getSum(values, x, y):
    sum = 0
    for xx in range(-1, 1 + 1):
        for yy in range(-1, 1 + 1):
#            print xx, yy, values[C + x + xx][C + y + yy]
            sum += values[C + x + xx][C + y + yy]
    return sum

values = numpy.zeros((200, 200))
values[C + 0][C + 0] = 1

x = 0
y = 0
d = 1
movesInDir = 0
turnsWithD = 0
vx = 1
vy = 0
for i in range(289326):
    j = i + 1
#    print j, x, y, abs(x) + abs(y)
    x += vx
    y += vy

    newValue = getSum(values, x, y)
    print j+1, newValue
    values[C + x][C + y] = newValue
    if newValue > 289326:
        print "!!!!", newValue
        break

    movesInDir += 1
    if movesInDir >= d:
        if vx == 1:
            vx = 0
            vy = 1
        elif vy == 1:
            vx = -1
            vy = 0
        elif vx == -1:
            vx = 0
            vy = -1
        else:
            vx = 1
            vy = 0
        movesInDir = 0
        turnsWithD += 1
        if turnsWithD >= 2:
            d += 1
            print "d", d
            turnsWithD = 0