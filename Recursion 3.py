# Complete the factorial function below.
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)
    
if __name__ == '__main__':
    n = int(input())
    print(factorial(n))