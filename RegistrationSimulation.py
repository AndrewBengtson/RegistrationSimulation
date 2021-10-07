import random
import copy
#this is an extremely simple simulation which implements bucket vs student-by-student class selection

class Student:
    name = ""
    desired = []
    reported = []
    registered = []
    def __init__(self,desired,name):
        self.desired =desired
        self.reported = desired
        self.name = name

class course:
    name = ""
    capacity = 3
    registered = 0 
    seats_wanted = 0
    def __init__(self,name):
        self.name = name

#we create 13 courses
possible_courses = []
for i in range(0,13):
    possible_courses.append(course("course"+str(i)))

#we create 30 students
students=[]
for i in range(0,30):
    #each student desires 10 of the classes in a random order
    wanted = copy.deepcopy(possible_courses)
    random.shuffle(wanted)
    #remove 3 items
    wanted.remove(wanted[0])
    wanted.remove(wanted[0])
    wanted.remove(wanted[0])
    new_student = Student(wanted,"Student"+str(i))
    students.append(new_student)

#round 1 of registration with bucket method
