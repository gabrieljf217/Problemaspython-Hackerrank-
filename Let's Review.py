t=int(input())
s=[]
for i in range(t):
    s.append(input())    
for i in range(t):
   even=""
   old=""
   for k in range(len(s[i])):
       if k%2==0:
           old+=s[i][k]
       else:
           even+=s[i][k]
   indexed=old+" "+even      
   print(indexed)