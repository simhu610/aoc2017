from knot_hash import knot_hash
# def knot_hash(k):
#     return "a5a5a5a5a5a5a5a5a5a5a5a5a5a5a5a5"

key = "vbqugkhl"
# key = "flqrgnkx"
used = 0
grid = []

for i in range(128):
    k = "{}-{}".format(key, i)
    h = knot_hash(k)
    s = "{0:b}".format(int(h, 16))
    n = [int(b) for b in s]
    used += sum(n)
    while len(n) < 128:
        n = [0] + n
    grid.append(n)

print used

print len(grid), len(grid[0])

import numpy as np
labels = np.zeros((128, 128), int)
max_label = 0

to_merge = {}

to_remove = set([])
change_to = {}

for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col]:
            candidates = []
            if row > 0 and labels[row - 1][col]:
                candidates.append(labels[row - 1][col])
            if col > 0 and labels[row][col - 1]:
                candidates.append(labels[row][col - 1])
            if len(candidates) == 1 or (len(candidates) == 2 and candidates[0] == candidates[1]):
                label = candidates[0]
            elif len(candidates) == 2:
                minc = min(candidates)
                maxc = max(candidates)
                while minc in change_to:
                    # print minc, change_to[minc]
                    minc = change_to[minc]
                while maxc in change_to:
                    maxc = change_to[maxc]
                label = minc
                if minc in to_merge:
                    to_merge[minc].add(maxc)
                else:
                    to_merge[minc] = set([maxc])
                to_remove.add(maxc)
                if minc != maxc:
                    if maxc in change_to:
                        change_to[maxc] = min(change_to[maxc], minc)
                    else:
                        change_to[maxc] = minc
            else:
                max_label += 1
                label = max_label
            # while label in change_to:
            #     label = change_to[label]
            if row == 127 and col < 15:
                print col, candidates, label
            labels[row][col] = label
    if row < 8:
        print labels[row][:8]

def p(y):
    if y in to_merge:
        print to_merge[y]
        for yy in to_merge[y]:
            p(yy)

print max_label

# p(87)
#
# print sorted(to_merge)
# print sorted(to_remove)
#
# merge_diff = 0
# to_remove2 = set([])
#
# for m in to_merge:
#     merge_diff += len(to_merge[m])
#     for mm in to_merge[m]:
#         to_remove2.add(mm)
#
# print merge_diff
# print max_label - merge_diff
#
# print len(to_remove)
# print max_label - len(to_remove)
#
# print len(to_remove2)
# print max_label - len(to_remove2)
# print sorted(to_remove2)
#
# print "change to", len(change_to)
# left = set([])
# for c in change_to:
#     left.add(change_to[c])
#
# print "left", len(left)
#
not_change = 0
for i in range(max_label):
    if i not in change_to:
        not_change += 1

print "not change", not_change
#
# # for k in sorted(change_to):
# #     print k, change_to[k]

labels2 = []

for row in labels:
    new_row = []
    for value in row:
        new_value = value
        while new_value in change_to:
            new_value = change_to[new_value]
        new_row.append(new_value)
    labels2.append(new_row)

for row in labels2[123:]:
    print np.array(row[:15])

# print change_to[2119]