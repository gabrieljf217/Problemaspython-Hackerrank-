# Complete the compareTriplets function below.
def compareTriplets(a, b):
    result=[0,0]
    for i in range(3):
        if a[i]>b[i]:
            result[0]+=1
        elif a[i]<b[i]:
            result[1]+=1
        elif a[i]==b[i]:
            continue
    return result
if __name__ == '__main__':

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))
    salida=[]
    salida=compareTriplets(a, b)
    
    print(salida[0],salida[1])
