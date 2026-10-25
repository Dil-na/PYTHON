name = 'Dilna'
course = "Python Fullstack"
address = '''
Kochi
Kerala
India
'''

print(name)
print(course)
print(address)
print(type(name))
print(course[0])
print(course[7])
print(course[15])
print(course[-1])
print(course[-6])
print(len(course))
# slicing [start:end:step]
print(course[0:5])
print(course[-10:-5])
print(course[:6])
print(course[6:])
print(course[2:10:2])
print(course[::2])
print(course[::-1])
for x in course:
    print(x)

course = "Python Fullstack"
print(course.upper())
print(course.lower())
print(course.capitalize())
print(course.title())
print(course.swapcase())
print(course.isupper())
print(course.islower())

print(course.index('Fullstack'))
print(course.count('l'))
print('3456'.isdigit())
print('abcd'.isalpha())
print('abc234'.isalnum())
print(' hlo '.strip())
print(' hai '.lstrip(),"hello")
print(' hai '.rstrip(),"hello",sep='-')
print(course.startswith("Py"))
print(course.endswith("stack"))

print(course.replace("PYTHON","Javascript"))
print(course.split(' '))
print(course.split('t'))
print(" ".join(["hello","world"]))
print("Name:",name,".\nCourse:",course)
print(f"Name: {name} .\nCourse: {course}.")
print("Name: {}.\nCourse: {}.".format(name,course))
print('-'*25)
print(f"{"Name":^10}{"Age":^5}{"Course":^10}")
print('-'*25)
print(f"{"Abhijith":<10}{"19:<5"}{"BCA":>10}")
print(f"{"Abhijith":<10}{"19:<5"}{"BCA":>10}")
print(f"{"Abhijith":<10}{"19:<5"}{"BCA":>10}")
print(f"{"Abhijith":<10}{"19:<5"}{"BCA":>10}")
print(f"{"Abhijith":<10}{"19:<5"}{"BCA":>10}")
print(f"{"Abhijith":<10}{"19:<5"}{"BCA":>10}")
print(f"{"Abhijith":<10}{"19:<5"}{"BCA":>10}")
print('-'*25)
