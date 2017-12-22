#1969
m=[r.strip() for r in open("22").readlines()]
x=y=(len(m)-1)/2
d=0
v=[[0,-1],[1,0],[0,1],[-1,0]]
i=0
for _ in range(10000000):
 c=m[y][x]
 if c=='#':
  d=(d+1)%4
  m[y]=m[y][:x]+'F'+m[y][x+1:]
 elif c=='.':
  d=(d-1)%4
  m[y]=m[y][:x]+'W'+m[y][x+1:]
 elif c=='W':
  m[y]=m[y][:x]+'#'+m[y][x+1:]
  i+=1
 elif c=='F':
  d=(d+2)%4
  m[y]=m[y][:x]+'.'+m[y][x+1:]
 x+=v[d][0]
 y+=v[d][1]
 w=len(m[0])
 h=len(m)
 q=range(h)
 if y>=h:
  m.append('.'*w)
 if y<0:
  m.insert(0,'.'*w)
  y+=1
 if x>=w:
  for yy in q:
   m[yy]+='.'
 if x<0:
  for yy in q:
   m[yy]='.'+m[yy]
  x+=1
print i
#2512261