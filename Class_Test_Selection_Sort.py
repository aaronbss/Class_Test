# https://github.com/aaronbss/Class_Test
""" In this program i am taking the input of the student details in 3 different arrays and then manipulating it in
order to sort, fetch & delete entries. The sorting method used here is selection sort since it has a quick retrieve
time and also sorts in an ascending order making it easier for the program to eliminate the student details with the
lowest student number"""

import time     # Importing the time function to display the sorting time.


class Student:

    def __init__(self, a=[], b=[], c=[]):            # Initialising the init function by specifying the input variables
        self.stud_num = a
        self.stud_nam = b
        self.course_num = c

    def add_value(self):
        n = int(input("Please enter the number of students you want to register"))
        for i in range(1, n+1):
            a = int(input("Please enter the student number"))
            if len(str(a)) < 9:                               # Ensuring the length of the entered number is less than 8
                self.stud_num.append(a)                       # Adding the number to the list
            else:
                print("You have entered a wrong student number")  # Exception message
                break                                                 # Breaks out of the loop and displays the message
            self.stud_nam.append(input("Please enter student name"))
            b = int(input("Please enter the course ID"))
            if len(str(b)) < 8:
                self.course_num.append(b)
            else:
                print("You have entered a wrong course id")
                break

        print("Names of students", self.stud_nam)
        print("Student Number", self.stud_num)
        print("Course Number", self.course_num)

    def retrieve(self):
        start_time = time.perf_counter()                # Timer Started
        for i in range(0, len(self.stud_num) - 1):      # For-loop to run the outer loop
            min_index = i                               # Assuming the first index value to be the minimum
            for j in range(i + 1, len(self.stud_num)):  # Second For-loop to run the inner loop
                if self.stud_num[j] < self.stud_num[min_index]:  # Comparing value of index one with index 0
                    min_index = j                        # if Value of index one is lower we reassign the lowest index
            if min_index != i:                           # We interchange values so that the arrays are Synchronous
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
        print("--- %s seconds ---" % (round(time.perf_counter()) - start_time))           # Retrieval Time calculation


obj = Student()
obj.add_value()
obj.retrieve()


