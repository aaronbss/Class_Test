class Student:

    def __init__(self, a=[], b=[], c=[]):
        self.stud_num = a
        self.stud_nam = b
        self.course_num = c

    def add_value(self):
        n = int(input("Please enter the number of students you want to register"))
        for i in range(1, n+1):
            self.stud_num[i].append(input("Please enter the Student number"))
            self.stud_nam[i].append(input("Please enter student name"))
            self.course_num[i].append(input("Please enter the course ID"))

    def retrieve(self):
        for k in range(2, len(self.stud_num)):
            if self.stud_num[1] < self.stud_num[k+1]:
                continue
            else:
                self.stud_num[1].replace(self.stud_num[k])
                self.stud_nam[1].replace(self.stud_nam[k])
                self.course_num[1].replace(self.course_num[k])

        print("The lowest student number, Name, Curse ID retrieved is", self.stud_num[1], self.stud_nam[1], self.course_num[1])


obj = Student()
