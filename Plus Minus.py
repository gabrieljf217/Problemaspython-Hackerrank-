#!/bin/python3
# Complete the plusMinus function below.
def plusMinus(arr):
    positive=0
    negative=0
    zero=0
    for i in range(len(arr)):
        if arr[i]<0:
            negative+=1
        elif arr[i]>0:
            positive+=1
        else:
            zero+=1
    return positive,negative,zero
            
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    p=plusMinus(arr)
    print("{:.6f}".format(p[0]/n))
    print("{:.6f}".format(p[1]/n))
    print("{:.6f}".format(p[2]/n))