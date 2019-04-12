def minion_game(string):
    Stuart=0
    Kevin=0
    for i in range(len(s)):
        if s[i] in 'AEIOU':
            Kevin+=(len(s)-i)
        else:
            Stuart+=(len(s)-i)
            
    if Kevin>Stuart:
        print("Kevin",Kevin)
    elif Kevin<Stuart:
        print("Stuart",Stuart)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)