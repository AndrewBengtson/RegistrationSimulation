import random
import copy
#this is an extremely simple simulation which implements bucket vs student-by-student class selection

class Student:
    name = ""
    desired = []
    reported = []
    registered = []
    def __init__(self,desired,name):
        self.desired =desired.copy()
        self.reported = desired.copy()
        self.registered = []
        self.name = name

class Course:
    name = ""
    capacity = 3
    registered = [] 
    students_who_want = []
    def __init__(self,name):
        self.name = name
        self.capacity = 3
        self.registered = [] 
        self.students_who_want = []

#we create 13 Courses
possible_courses = []
for i in range(0,2):
    possible_courses.append(Course("course"+str(i)))

#we create 30 students
students=[]
for i in range(0,5):
    #each student desires the classes in a random order
    wanted = (possible_courses).copy()
    random.shuffle(wanted)
    new_student = Student(wanted,"Student"+str(i))
    students.append(new_student)

#round 1 of registration with bucket method
for student in students:
    #first iterate through all students and update their most desired class
    most_desired = student.desired[0]
    most_desired.students_who_want.append(student)
#now index all possible classes,
for course in possible_courses:
    #in the case where the number of students who want to take the class is reasonable just sign them up
    if(len(course.students_who_want)<=course.capacity):
        course.registered = course.students_who_want.copy()
        for student in course.registered:
            student.registered.append(course)
    #in the case of overflow
    else:
        #shuffle the list of students who want to get in
        random.shuffle(course.students_who_want)
        #register the students within capacity
        course.registered = course.students_who_want[:course.capacity]
        for student in course.registered:
            student.registered.append(course)
#now we look at the students and see how many got what they wanted
for student in students:
    print(student.name,"wanted",student.desired[0].name,"and got",student.registered[0].name if (len(student.registered)>0) else "nothing")

        
    
        