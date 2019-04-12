#!/bin/python3
# Complete the staircase function below.
def staircase(n):
    for i in range(n):
        print(int(n-1-i)*" "+int(i+1)*"#")  
if __name__ == '__main__':
    n = int(input())
    staircase(n)

    