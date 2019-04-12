n=int(input())
ar=[]
ar=input()
ar=list(map(int,ar.split()))
arnew = list(set(ar))
salida=0
for i in range(len(arnew)):
    if ar.count(arnew[i])%2==0:
        salida+=ar.count(arnew[i])/2
    elif ar.count(arnew[i])>=3:
        num=(ar.count(arnew[i])-1)/2
        salida+=+num
        
print(int(salida)) 