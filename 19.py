# m = open("19_test").readlines()
# assert len(m) == 6
# for i in range(len(m)):
#     while len(m[i]) < 16:
#         m[i] += ' '
# assert all([len(m[i]) == 16 for i in range(len(m))])
m = open("19").readlines()

y = 0
x = m[y].find('|')
vx = 0
vy = 1

letters = ""
steps = 1

while True:
    assert m[y][x] != ' '
    if m[y][x] not in ['|', '-', '+']:
        print "Letter!", m[y][x]
        letters += m[y][x]
    print x, y, vx, vy
    x += vx
    y += vy
    steps += 1
    if m[y][x] == '+':
        print "Turn!"
        if vx == 0 and m[y][x - 1] != ' ':
            vx = -1
            vy = 0
        elif vx == 0 and m[y][x + 1] != ' ':
            vx = 1
            vy = 0
        elif vy == 0 and m[y - 1][x] != ' ':
            vx = 0
            vy = -1
        elif vy == 0 and m[y + 1][x] != ' ':
            vx = 0
            vy = 1
        else:
            print "The end!"
            break
    elif m[y][x] == ' ':
        steps -= 1
        print "The end!"
        break

print letters, steps