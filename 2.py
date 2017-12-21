import numpy
f = open("2_input")
checksum = 0
checksum2 = 0
for line in f.readlines():
    values = [int(x) for x in line.split()]
    checksum += max(values) - min(values)
    for i, value in enumerate(values):
        for value2 in values[i+1:]:
            if (float(value) / float(value2)) % 1 == 0:
                checksum2 += value / value2
            if (float(value2) / float(value)) % 1 == 0:
                checksum2 += value2 / value
print
print checksum
print
print checksum2