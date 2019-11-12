# Complete the twoStrings function below.
def twoStrings(s1, s2):
    salida, letra = 0, 0
    while letra < (len(s1)):
        salida = 1 if s1[letra] in s2 else salida
        letra+=1
    print("YES") if salida == 1 else print("NO")           
    
q = int(input())
for q_itr in range(q):
    s1 = input()
    s2 = input()
    result = twoStrings(s1, s2)