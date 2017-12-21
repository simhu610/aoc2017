x=list(map(int,open("5")))
i=s=0
while 0<=i<len(x):
 o=i
 i+=x[i]
 x[o]+=-1if x[o]>2 else 1
 s+=1
print s