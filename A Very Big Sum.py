def aVeryBigSum(ar):
    suma=0
    for i in range(len(ar)):
        suma+=ar[i]
    return suma
if __name__ == '__main__':
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = aVeryBigSum(ar)
    print(str(result) + '\n')