from mathfunction import PI, add, subtract, multiply, divide

print (PI)
while True:
    choice = input('+--> Add\n---> Subtract\n*--> Multiply\n/--> Divide\nq--> Quit\nEnter your choice: ')
    try:
        n1 = int(input('Enter first number: '))
        n2 = int(input('Enter second number: '))
    except ValueError:
        print("Integers are only allowed.")
        continue
    match choice.strip():
        case '+':
            print(add(n1, n2))
        case '-':
            print(subtract(n1, n2))
        case '*':
            print(multiply(n1, n2))
        case '/':
            print(divide(n1, n2))
        case 'q':
            break
        case _:
            print("Invalid choice. Please try again.")

# import module_name
# module_name.function_name()
# module_name.variable

# import module_name as alias
# alias.function_name()
# alias.variable

# from module_name import *
# function_name1()
# function_name2()
# variable

# from module_name import function_name,variable
# function_name()
# variable