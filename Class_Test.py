class Student:
    def __init__(self):
        self.stud_num = []
        self.stud_nam = []
        self.course_num = []
        n = int(input("Please enter the number of students ou want to register"))
        for i in range(1, n+1):
            self.stud_num[i] = input("Please enter the Student Number ")
            self.stud_nam[i] = input("Please enter the Student Name")
            self.course_num = input("Please enter the Course Number")

    def retrieve(self):
        for i in range(2, len(self.stud_num)):
            if self.stud_num[1]<self.stud_num[i+1]:
                continue
            else:
                self.stud_num[1] = self.stud_num[i]

        print("The lowest student number retrieved is", self.stud_num[1])


num = retrieve()

###x