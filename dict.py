student ={
    "name":"Dilna",
    "course":"python",
    "student_id":"SYN121",
    "student_id":"SYN111",
    "Age":"22",
    "hobbies":["Reading","Gaming"]
}
d1 = {}  #empty dict 
s1 = set () #empty set
print(student)
print(type(student))
print(type(d1))
print(type(s1))
student["course"] = "python programming"
student["full_name"] = " Dilna m"
print(student["name"])
print(student)

items = student.items()
for a in student:
    print(student[a])

print("name" in student)
print(student["course"])
print(student.get("coursee"))
print(student.get("coursee","not applicable"))
student.update({"course":"python programming"})
student.update({"place":"kochi"})
student.setdefault("age",24)
student.pop("student_id")
student.popitem()
print(student)

print(student.keys())
print(student.values())
print(student.items())

for key,value in items:
    print(f"{key:<10}:{value}")

d2 =dict([("emp_No", 758649),("emp_name","parthiv"),("department","software")])
print(d2)

copy_std = student.copy()
copy_std['course']="MERN"
copy_std['hobbies'][0]="singing"
print(copy_std)
print(student)