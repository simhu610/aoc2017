
def add(i, linked, x):
    if not i in linked:
        linked.append(i)
        for b in x[i]:
            add(b, linked, x)

x = {}
y = open("12").readlines()
for line in y:
    l = line.split()
    a = int(l[0])
    b = [int(ll.replace(',', '')) for ll in l[2:]]
    x[a] = b
    # break

# linked = []
#
# add(0, linked, x)
#
# print len(linked)

groups = []

for key in x:
    if not any([key in g for g in groups]):
        new_group = []
        add(key, new_group, x)
        groups.append(new_group)

print len(groups)