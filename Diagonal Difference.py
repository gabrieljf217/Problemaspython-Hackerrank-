# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    left=0
    right=0
    l=0
    for i in range(len(arr)):
        left+=arr[i][i]
    for k in range(len(arr)-1,-1,-1):
        right+=arr[k][l]
        l+=1
        
    return abs(left-right)
    
if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    print(result)