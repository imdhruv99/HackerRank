class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    
    def __init__(self, firstName, lastName, idNumber, testScores):
        super().__init__(firstName, lastName, idNumber)
        self.testScores = testScores
        
    def calculate(self):
        
        total = 0
        
        for score in self.testScores:
            
            total += score
        
        average = total / len(self.testScores)
        
        if 90 <= average <= 100:
            return 'O'
        if 80 <= average < 90:
            return 'E'
        if 70 <= average < 80:
            return 'A'
        if 55 <= average < 70:
            return 'P'
        if 40 <= average < 55:
            return 'D'
        return 'T'

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())