import numpy
f = open("1_input")
checksum = 0
listOfInts = []
for line in f.readlines():
    print "LINE"
    prev = 8
    print len(line)
    for c in line:
        try:
            i = int(c)
            listOfInts.append(i)
            if i == prev:
                checksum += i
            prev = i
        except:
            print c
print checksum

print len(listOfInts)
sum2 = 0
for i, val in enumerate(listOfInts):
    if val == listOfInts[(i + len(listOfInts) / 2) % len(listOfInts)]:
        sum2 += val
print sum2