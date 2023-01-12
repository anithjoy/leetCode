# create 2 classes. 
# students and course
# inside student class. take input name and grade
# create function for getting grade
# inside course take maximum number of students as an input and course name as an input
# insert student object into course object

"""
class student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade

    def getGrade(self):
        return self.grade


class course:
    def __init__(self,courseName,max):
        self.courseName = courseName
        self.max = max
        self.students = []

    def addStudent(self,student):
        if len(self.students) < self.max:
            self.students.append(student)
            return len(self.students)

        return False

    def avgGrade(self):
        total = 0
        for student in self.students:
            total += student.getGrade()

        return total/len(self.students)
 

s1 = student("anith",85)
s2 = student("bob",95)
s3 = student("carl",85)

c1 = course("Math",3)
c2 =  course("English",3)
c3 = course("OOP",2)

ans = c1.addStudent(s1)
ans = c1.addStudent(s2)
ans = c1.addStudent(s3)

ans = c3.addStudent(s1)
ans = c3.addStudent(s2)
ans = c3.addStudent(s3)

ans = c1.students[0].name

ans = c3.avgGrade()
ans = c1.avgGrade()




print(ans) """


########################################################################################
#  Done with classes and objects and how to create new objects
########################################################################################


# INHERITANCE
# The below code explains about mulitple inheritance
# super() key word is used to refer the parent class

"""
class joy:
    def __init__ (self,name,relation):
        self.name = name
        self.relation = relation
        print(f"Joy  __init__ is called --->{self.name} --->{self.relation}")

    def printJoy(self):
        print(" Hey i am joy")

class regini():
    def printRegini(self):
        print(" Hey i am regini")

class anith(joy,regini):

    def printAnith(self):
        print(" Hey i am anith")

class anoop(joy):
    def __init__(self,name,relation,profession):
        super().__init__(name,relation)
        self.profession = profession
        print(f"Anoop  __init__ is called--->{self.name} --->{self.relation} --->{self.profession}")

    def printAnoop(self):
        print(" Hey i am anoop")

obj1 = joy("k n Joy","Father")

print("---------------------------------------------")
obj2 = anoop("anoop","son","engineer")

# obj1.printJoy()
# obj1.printRegini()
# obj1.printAnith()

"""

########################################################################################
#  Done with INHERTIANCE
########################################################################################


# classmethod()

class person:
    nop = 0

    def __init__(self,name):
        self.name = name
        person.add_nop()
        

    @classmethod
    def number_of_people(cls):
        return cls.nop

    @classmethod
    def add_nop (cls):
        cls.nop += 1

p1 = person("p1")
p2 = person("p2")
p3 = person("p3")


print(person.nop)