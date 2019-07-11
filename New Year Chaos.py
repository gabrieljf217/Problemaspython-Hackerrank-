#!/bin/python3

# Complete the minimumBribes function below.
def minimumBribes(q):
    moves = 0
    for i in range(len(q)-1,-1,-1):
        if q[i] - (i + 1) > 2:
            return print('Too chaotic')
        for k in range(max(0, q[i] - 2),i):
            if q[k] > q[i]:
                moves+=1
    print(moves)

t = int(input())

for t_itr in range(t):
    n = int(input())

    q = list(map(int, input().rstrip().split()))

    minimumBribes(q)