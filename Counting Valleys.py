def countingValleys(n, s):
    sea=0
    sean=0
    valley=0
    for i in range(len(s)):
        caracter=s[i]
        if caracter=='U':
            sean=sea
            sea+=1
        else:
            sean=sea
            sea-=1
        if sean==-1 and sea==0:
            valley+=1
                
    return valley

if __name__ == '__main__':
    n = int(input())
    s = input()
    result = countingValleys(n, s)
    print(str(result))

