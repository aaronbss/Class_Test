class Student:

    def __init__(self, a=[], b=[], c=[]):
        self.stud_num = a
        self.stud_nam = b
        self.course_num = c

    def add_value(self):
        n = int(input("Please enter the number of students you want to register"))
        for i in range(1, n+1):
            self.stud_num.append(int(input("Please enter the student number")))
            self.stud_nam.append(input("Please enter student name"))
            self.course_num.append(int(input("Please enter the course ID")))

        print(self.stud_nam)
        print(self.stud_num)
        print(self.course_num)

    def retrieve(self):
        for j in range(0, 1):
            for k in range(1, len(self.stud_num)):
                if self.stud_num[j] < self.stud_num[k]:
                    continue
                else:
                    self.stud_num[j] = (self.stud_num[k])
                    self.stud_nam[j] = (self.stud_nam[k])
                    self.course_num[j] = (self.course_num[k])

        for i in range(0, 1):
            print("The lowest student number, Name, Course ID retrieved is", self.stud_num[i], self.stud_nam[i], self.course_num[i])


obj = Student()
obj.add_value()
obj.retrieve()
