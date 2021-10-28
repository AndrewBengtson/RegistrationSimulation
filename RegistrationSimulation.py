import random
import copy
#this is an extremely simple simulation which implements bucket vs student-by-student class selection

#these are dummy students used for the simulation, will be replaced by the database
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
#these are dummy Courses used for the simulation, will be replaced by the database
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
#round 1 of registration with bucket method
def bucket_register(students,possible_courses):
    for student in students:
        #first iterate through all students and update their most desired class
        most_desired = student.reported[0]
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
#For the sake of the simulation, prereqs and timing are ignored
def ClassIsOpen(student,course):
    #Check that class has a seat open
    if not (len(course.registered)<course.capacity):
        return False
    #Check that class time does not overlap with current student schedule
        #If not, return False
    #Check that student is eligible for class
        #For each restriction of class (social class, major, prereqs, instructor permission), check the appropriate student data.
        #If any fails, return False
    #IGNORING CO-REQS FOR RELEASE 1
    return True

def student_register(students,possible_courses):
    #we index the list of students first
    for student in students:
        #we try to register the student for classes in their order of preference
        index = 0
       # print(student.name,"wants",student.desired[0].name," ",student.desired[1].name)
        registered = False
        while(index<len(student.reported) and not registered):
            #if there is a seat available put the student in it
            if(len(student.reported[index].registered)<student.reported[index].capacity and student.reported[index] not in student.registered):
                student.registered.append(student.reported[index])
                student.reported[index].registered.append(student)
                registered = True
                #print(student.name,"got",student.reported[index].name,"as their ",index,"choice")
            #if there is not a seat available we just keep the loop
            index+=1
        #print(student.name," got nothing")
    #now we look at the students and see how many got what they wanted
    for student in students:
        wanted = []
        for report in student.reported:
            wanted.append(report.name)
        and_got = []
        for register in student.registered:
            and_got.append(register.name)
        print(student.name,"wanted",wanted,"and got",and_got)

#we create 13 Courses
possible_courses = []
for i in [301,303,304,312]:
    possible_courses.append(Course("CSCI"+str(i)))

#we create 30 students
students=[]
bucket_students = []
for i in ["Andrew","Jeannine","Robert","Peter"]:
    #each student desires the classes in a random order
    wanted = (possible_courses).copy()
    random.shuffle(wanted)
    new_student = Student(wanted,str(i))
    students.append(new_student)
    bucket_student = Student(wanted.copy(),"Student"+str(i))
    bucket_students.append(bucket_student)

#clean out all of the courses
for course in possible_courses:
    course.registered = []
    course.students_who_want = []

for i in range(1,4):
    print("-----ROUND "+str(i)+"-----")
    student_register(students,possible_courses)
    random.shuffle(students)

        
    
        