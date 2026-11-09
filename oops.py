# class ClassName:
# attribute
# methods
# pass

# class Student:
#     college = "IIET"
#     def attendance(self,is_present):
#         print(f"Student is {'present' if is_present else 'absent'}")

# std1 = Student()
# std2 = Student()
# std2.college = "IGGIS"
# print(std1.college)
# print(std2.college)

# print(std1)
# print(std2)
# print(type(std1))
# print(type(std2))

# std1.attendance(True)
# std2.attendance(False)


class Student:
    def __init__(self, name, rno, marks):
        self.name = name
        self.rno = rno
        self.marks = marks
        self.attendance = False
    def mark_attendence(self, is_present):
        self.attendance = is_present
    def Student_details(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.rno}")
        print(f"Total: {sum(self.marks)}")
std1 = Student("Anu", 1, [90, 80, 70])
std2 = Student("Amal", 2, [85, 75, 65])
std1.name = 'Aleena'

print(std1.name)
print(std2.name)
std1.mark_attendence(True)
std1.Student_details()