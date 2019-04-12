def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i]<=37:
            continue
        if grades[i]%5 >= 3:
            add=5-grades[i]%5
            grades[i]+=add
        else:
            continue
    return grades

if __name__ == '__main__':
    n = int(input())
    grades = []
    for _ in range(n): 
        grades.append(int(input()))
    result = gradingStudents(grades)
    for i in range(len(result)):
        print(str(result[i]))