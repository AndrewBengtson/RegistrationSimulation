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
#round 1 of registration with bucket method
def bucket_register(students,possible_courses):
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

def student_register(students,possible_courses):
    #we index the list of students first
    for student in students:
        #we try to register the student for classes in their order of preference
        index = 0
       # print(student.name,"wants",student.desired[0].name," ",student.desired[1].name)
        registered = False
        while(index<len(student.desired) and not registered):
            #if there is a seat available put the student in it
            if(len(student.desired[index].registered)<student.desired[index].capacity):
                student.registered.append(student.desired[index])
                student.desired[index].registered.append(student)
                registered = True
                #print(student.name,"got",student.desired[index].name,"as their ",index,"choice")
            #if there is not a seat available we just keep the loop
            index+=1
    #now we look at the students and see how many got what they wanted
    for student in students:
        print(student.name,"wanted",student.desired[0].name,"and got",student.registered[0].name if (len(student.registered)>0) else "nothing")

#we create 13 Courses
bucket_possible_courses = []
possible_courses = []
for i in range(0,2):
    bucket_possible_courses.append(Course("course"+str(i)))
    possible_courses.append(Course("course"+str(i)))

#we create 30 students
students=[]
bucket_students = []
for i in range(0,5):
    #each student desires the classes in a random order
    wanted = (bucket_possible_courses).copy()
    random.shuffle(wanted)
    new_student = Student(wanted,"Student"+str(i))
    students.append(new_student)
    bucket_student = Student(wanted.copy(),"Student"+str(i))
    bucket_students.append(bucket_student)
#call the bucket registration process
bucket_register(bucket_students,bucket_possible_courses)
print("-----")
#clean out all of the courses
for course in bucket_possible_courses:
    course.registered = []
    course.students_who_want = []
student_register(students,possible_courses)

        
    
        