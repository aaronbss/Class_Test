# https://github.com/aaronbss/Class_Test
""" In this program i am taking the input of the student details in 3 different arrays and then manipulating it in
order to sort, fetch & delete entries. The sorting method used here is selection sort since it has a quick retrieve
time and also sorts in an ascending order making it easier for the program to eliminate the student details with the
lowest student number"""


class Student:

    def __init__(self, a=[], b=[], c=[]):
        self.stud_num = a
        self.stud_nam = b
        self.course_num = c

    def add_value(self):
        n = int(input("Please enter the number of students you want to register"))
        for i in range(1, n+1):
            try:
                a = int(input("Please enter the student number"))
                if len(a) < 9:
                    self.stud_num.append(a)
            except:
                print("You have entered wrong student number")
            self.stud_nam.append(input("Please enter student name"))
            self.course_num.append(int(input("Please enter the course ID")))

        print("Names of students", self.stud_nam)
        print("Student Number", self.stud_num)
        print("Course Number", self.course_num)

    def retrieve(self):
        for i in range(0, len(self.stud_num) - 1):
            min_index = i
            for j in range(i + 1, len(self.stud_num)):
                if self.stud_num[j] < self.stud_num[min_index]:
                    min_index = j
            if min_index != i:
                self.stud_num[i], self.stud_num[min_index] = self.stud_num[min_index], self.stud_num[i]
                self.stud_nam[i], self.stud_nam[min_index] = self.stud_nam[min_index], self.stud_nam[i]
                self.course_num[i], self.course_num[min_index] = self.course_num[min_index], self.course_num[i]

        for i in range(0, 1):
            print("The lowest student number, Name, Course ID retrieved is", self.stud_num[i], self.stud_nam[i], self.course_num[i])
            self.stud_num.remove(self.stud_num[i])
            self.stud_nam.remove(self.stud_nam[i])
            self.course_num.remove(self.course_num[i])

        print("Updated list of Students")
        print("Names of students", self.stud_nam)
        print("Student Number", self.stud_num)
        print("Course Number", self.course_num)


obj = Student()
obj.add_value()
obj.retrieve()


