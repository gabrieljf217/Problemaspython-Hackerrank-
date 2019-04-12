n = int(input())
nt={}
names=[]
for i in range(n):
    ntalt=list(input().rstrip().split())
    nt.update({ntalt[0]:int(ntalt[1])})
    ntalt=[]
for i in range(n):
    names.append(input())

for i in range(n):
    valor=nt.get(names[i])
    if valor==None:
        print("Not found")
    else:
        print(names[i]+"="+str(valor))
    