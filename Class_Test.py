class Student:
    def __init__(self, stud_num, stud_nam, course_num):
        self.stud_num = [8]
        self.stud_nam = []
        self.course_num = [7]
        n = int(input("Please enter the number of students ou want to register"))
        for i in range(1, n+1):
            self.stud_num[i] = input("Please enter the Student Number ")
            self.stud_nam[i] = input("Please enter the Student Name")
            self.course_num = input("Please enter the Course Number")

    def retrieve(self):
        








obj = Student("10758","Aaron", "20A")