import numpy as np

m = [row.strip() for row in open("22").readlines()]
#m = ["..#", "#..", "..."]

x = y = (len(m) - 1) / 2
dir = 0

v = [{'x': 0, 'y': -1},
     {'x': 1, 'y': 0},
     {'x': 0, 'y': 1},
     {'x': -1, 'y': 0}]

infections = 0

iterations = 10000000

import time
t0 = time.time()

for iteration in range(iterations):
    # print float(iteration) / iterations
    # if m[y][x] == '#':
    #     dir = (dir + 1) % 4
    #     m[y] = m[y][:x] + '.' + m[y][x + 1:]
    # else:
    #     assert m[y][x] == '.', "unknown char ({})".format(m[y][x])
    #     dir = (dir - 1) % 4
    #     m[y] = m[y][:x] + '#' + m[y][x + 1:]
    #     infections += 1
    if m[y][x] == '#':
        dir = (dir + 1) % 4
        m[y] = m[y][:x] + 'F' + m[y][x + 1:]
    elif m[y][x] == '.':
        dir = (dir - 1) % 4
        m[y] = m[y][:x] + 'W' + m[y][x + 1:]
    elif m[y][x] == 'W':
        m[y] = m[y][:x] + '#' + m[y][x + 1:]
        infections += 1
    elif m[y][x] == 'F':
        dir = (dir + 2) % 4
        m[y] = m[y][:x] + '.' + m[y][x + 1:]
    x += v[dir]['x']
    y += v[dir]['y']
    # print x, y, dir
    width = len(m[0])
    height = len(m)
    # print width, height
    if y >= height:
        m.append('.' * width)
    elif y < 0:
        m.insert(0, '.' * width)
        y += 1
    elif x >= width:
        for yy in range(height):
            m[yy] += '.'
    elif x < 0:
        for yy in range(height):
            m[yy] = '.' + m[yy]
        x += 1

    # assert all([len(row) == len(m[0]) for row in m])

t1 = time.time()

for y_row, row in enumerate(m):
    if y_row == y:
        if row[x] == '#':
            print row[:x] + 'X' + row[x + 1:]
        elif row[x] == 'W':
            print row[:x] + 'w' + row[x + 1:]
        elif row[x] == 'F':
            print row[:x] + 'f' + row[x + 1:]
        else:
            print row[:x] + ':' + row[x + 1:]
    else:
        print row
print "--------------"

print infections

print t1 - t0, "seconds"