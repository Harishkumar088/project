import math
import os
import re
def fileconv(i,j):
    u=open(i,"r").read().lower()
    u=re.sub('[^a-z\ \']+',"",u)
    u=u.split(" ")
    z=open(j,"r").read().lower()
    z=re.sub('[^a-z\ \']+',"",z)
    z=z.split(" ")
    return u,z
def d1(n):
    d1={ }
    for i in range(len(n)):
        d1[n[i]]=n.count(n[i])
    return(d1)
    print(d1)
def dot(x,y):
        dot=0
        for i in x:
            if i in y:
                dot=dot+(x.get(i)*y.get(i))
               # print(dot)
        return (dot)
        print(dot)
def v(d):
    v=0
    for i in d:
        v=v+(d.get(i)**2)
    v=math.sqrt(v)
    return(v)        
cwd = os.getcwd()
files = os.listdir(cwd)
files_txt = [i for i in files if i.endswith('.txt')]
print(files_txt)
le = len(files_txt)

for x1 in files_txt:
    for x2 in files_txt:
        
        if (files_txt.index(x1)<=files_txt.index(x2)):
            pass
        else:
            (s1,s2)= fileconv(x1,x2)
    

            #x=s1.read()
            #y=s2.read()

            # p=x.lower()
            # q=y.lower()
            # print(p)


            # s1=p.split(' ')
            # s1.sort()

            # s2=q.split(' ')
            # s2.sort()

            a=d1(s1)
            #print(a)

            b=d1(s2)
            print(b)
            c=dot(a,b)
            #print (c)
            v1=v(a)
            v2=v(b)
            print(v1)
            print(v2)

            m=c/(v1*v2)
            print(m)
            print(m*100,'%')
