#Create  a file and write the records of 10 students then read back all the records and find the  students detail who has the highest marks
class Student:
    def __init__(self, name = None, marks = None ):
        self.name = name
    def setMarks(self,marks):
        self.marks = marks
        
    def getName(self):
        return self.name
    def getMarks(self):
        return self.marks
no_of_Students = int(input("No of Students....."))
records = []
i = 0
import pickle
f_obj = open("records1.dat","ab")
while i<no_of_Students:
    name = input("Name: ")
    marks = float(input("Marks: "))
    temp = Student()
    pickle.dump(temp, f_obj)
    i = i+1
f_obj.close()
f_obj = open("records1.dat","rb")
while True:
    record = pickle.load(f_obj)
    print(record.getName(), record.getMarks())