n = int(input())
cont=0
aux=0
result=0
binn=bin(n)
for i in range(len(binn)):
    aux=binn[i]
    if aux=='1':
        cont+=1
    else:
        if cont>=result:
            result=cont
        cont=0
if cont>=result:
    result=cont
print(result)
