
a = 883
b = 879
# a = 65
# b = 8921

af = 16807
bf = 48271

d = 2147483647

m = 0

al = []
bl = []

# for i in range(40000000):
while True:
    a = a * af % d
    b = b * bf % d
    if a % 4 == 0:
        al.append(a)
    if b % 8 == 0:
        bl.append(b)
    if len(al) >= 5000000 and len(bl) >= 5000000:
        break

print len(al), len(bl)

for a, b in zip(al[:5000000], bl[:5000000]):
    if a&pow(2,16)-1==b&pow(2,16)-1:
        m += 1
    # if i % 400000 == 0:
    #     print i / 40000000.0

print m

