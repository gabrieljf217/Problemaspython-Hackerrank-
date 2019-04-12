arr = []
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))
hourglassfin=-100
for i in range(4):
    for j in range(4):
        hourglass=0 
        hourglass+=arr[i][j]
        hourglass+=arr[i][j+1]
        hourglass+=arr[i][j+2]
        hourglass+=arr[i+1][j+1]
        hourglass+=arr[i+2][j]
        hourglass+=arr[i+2][j+1]
        hourglass+=arr[i+2][j+2]
        hourglassfin=max(hourglass,hourglassfin)
print(hourglassfin)