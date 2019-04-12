def simpleArraySum(ar):
    arsum=0
    for i in range(len(ar)):
        arsum+=ar[i]
    return (arsum)

if __name__ == '__main__':
    
    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    print(simpleArraySum(ar))

   