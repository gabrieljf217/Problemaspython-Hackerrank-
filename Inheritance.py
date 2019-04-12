class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):  
    def __init__(self, firstName, lastName, idNumber,score):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.score = score
    def calculate(self):
        suma=sum(scores)
        promedio=suma/len(scores)
        if promedio>=90:
            return "O"
        elif promedio>=80:
            return "E"
        elif promedio>=70:
            return "A"
        elif promedio>=55:
            return "P"
        elif promedio>=40:
            return "D"
        else:
            return "T"

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
