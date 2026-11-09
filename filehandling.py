# open('filename','mode')
file = open('names.txt', 'r')# Open the file in read mode

print(file.read())  # Read the contents of the file and print it
print(file.read(5))
print(file.read(7))
print(file.read(8))
print(file.readline())  # Read a single line from the file
print(file.readlines())  # Read all lines from the file and return them as a list
file = open('names.txt', 'a')  # Open the file in append mode
file = open('names.txt', 'w')  # Open the file in write mode
file.write('anu\n')  # Write a string to the file
file.write('Amal\n')  # Write another string to the file    
file.write('Aleena\n')  # Write another string to the file
file.writelines(['anu\n', 'Amal\n', 'Aleena\n'])  # Write a list of strings to the file
file = open('students.txt', 'r')  # Open the file in read mode
file.close()  # Close the file

with open('names.txt', 'r') as file:  # Open the file in read mode using a context manager
    print(file.read(4))  # Read the contents of the file and print it
    print(file.read(5))  # Read the contents of the file and print it
    print(file.tell())  # Get the current position of the file pointer
    file.seek(16) # Move the file pointer to a specific position
    print(file.read(5))  # Read the contents of the file and print it

import os
print(os.path.exists('names.txt'))  # Check if the file exists
