l=open("f").readlines()
v=len(l)
for m in l:
 c=[]
 for x in m.split():
  if any([sorted(z)==sorted(x) for z in c]):
   v-=1
   break
  c.append(x)
print v