#!/bin/python3

# Complete the rotLeft function below.
def rotLeft(a, d):
    for i in range(d):
        value = a[0]
        a.pop(0)
        a.insert(len(a),value)
    return a

nd = input().split()
n = int(nd[0])
d = int(nd[1])
a = list(map(int, input().rstrip().split()))

result = rotLeft(a, d)
print(' '.join(map(str, result)))
