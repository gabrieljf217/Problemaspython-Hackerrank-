nm = input().split()
n = int(nm[0])
m = int(nm[1])
arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

k = int(input())

array = sorted(arr, key=lambda arr_entry: arr_entry[k])

for i in range(n):
    for j in range(m):
        print(array[i][j],end=' ')
    print(' ')