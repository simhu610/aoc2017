a=open("11").read().strip().split(',')
x=y=z=0
u={'n':0,'s':0,'nw':-2,'ne':2,'sw':-2,'se':2}
v={'n':2,'s':-2,'nw':1,'ne':1,'sw':-1,'se':-1}
for b in a:
 x+=u[b]
 y+=v[b]
 w=y+abs(x)/2
 z=max([z,w])
print w/2,z/2