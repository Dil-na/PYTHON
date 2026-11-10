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

# class childclass(ParentClassName):Derived , sub,child class
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def details(self):
#         print(self.name)
#         print(self.age)


# class Student(Person):
#     def __init__(self, name, age, rno, marks):
#         super().__init__(name, age)
#         print('init in child')
#         self.rno = rno
#         self.marks = marks
#         self.attendance = False
#     # def mark_attendence(self, is_present):
#     #     self.attendance = is_present
#     def Student_details(self):
#         super().details()
#         print(f"Roll No: {self.rno}")
#         print(f"Total: {sum(self.marks)}")
# std1 = Student("Anu", 20, 1, [90, 80, 70])

# print(std1.name)
# std1.details()

# std1 = Student("Anu", 1, 1, [90, 80, 70])
# std2 = Student("Amal", 2, 2, [85, 75, 65])
# std1.name = 'Aleena'

# print(std1.name)
# print(std2.name)
# std1.mark_attendence(True)
# std1.Student_details()


# import math
# from abc import ABC,abstractmethod

# class shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
       
# class Circle(shape):
#     def area(self,r):
#         print(math.pi*r*r)

# c1 = Circle()
# c1.area(5)

# import random
# user = input('Enter ur choice:')
# compter = random.choice(['rock','paper','scissors'])
# print(f"Computer choice: {compter}")
# print(f"Your choice: {user}")

class InvalidAgeError(Exception):
    pass
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise InvalidAgeError("Age must be greater than zero.")
except ValueError:
    print("Use only integers")
except InvalidAgeError as e:
    print(e)