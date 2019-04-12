def miniMaxSum(arr):
    max=0
    min=0
    arr.sort()
    for i in range(4):
        min+=arr[i] 
    for i in range(len(arr)-1,0,-1):
        max+=arr[i]
    return min,max
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    print(miniMaxSum(arr)[0],miniMaxSum(arr)[1])
    