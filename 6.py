import copy,numpy
x=map(int, open("6").read().split())
s=[]
while 1:
 if x in s:
  print len(s),len(s)-s.index(x)
  break
 s.append(copy.deepcopy(x))
 i=numpy.argmax(x)
 d=x[i]
 x[i]=0
 while d>0:
  i=(i+1)%len(x)
  x[i]+=1
  d-=1