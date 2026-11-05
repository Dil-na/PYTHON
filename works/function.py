# def function_name(parameter):
#     # function body
#     return 'result'

# function_name(arguments)

def greet():
    print(f"Hello")
greet()

def greet(user):
    print(f"Hello, {user}!")
greet("Alice") #call with argument

def greet(user):
    return f"Hello, {user}!"
result = greet("Bob") #call with argument
print(result)

def greet(msg,user='Guest'):
    return f"Hello, {user}!! {msg}..."

result1 = greet("Welcome to the platform")
result2 = greet("Welcome to the platform", "Alice")
print(result1)
print(result2)

def add (a,*args):
    sum = 0
    for n in args:
        sum += n
    return (f"Sum is: {sum}")

add("hello",45,86)
add(45, 86, 12) #arbitrary number of arguments
add(45, 86, 12, 34, 56, 78) 
add(45, 86, 12, 34, 56, 78, 90, 100)

print(1)
print(1,2)
print(1,2,3)
print(1,2,3,4)

def greet(msg,user):
    return f"Hello, {user}!! {msg}..."

print(greet(user='jithu', msg='Welcome to the platform')) #keyword arguments

def greet(**kwargs):
    print(kwargs)
greet(user= "Alice", msg="Welcome to the platform") #arbitrary keyword arguments


#calculator
def add (a,b):
    return a+b
def subtract (a,b):
    return a-b  
def multiply (a,b):
    return a*b
def divide (a,b):
    return a/b
while True:
    choice = input('+---> Addition\n- ---> Subtraction\n* ---> Multiplication\n/ ---> Division\nq ---> Quit\nEnter your choice: ')
    try:
        n1 = int(input("Enter first number: "))
        n2 = int(input("Enter second number: "))
    except ValueError:
        print("Only integers are allowed..")
        continue
    match choice.strip():
        case '+':
            print(add(n1,n2))
        case '-':
            print(subtract(n1,n2))
        case '*':
            print(multiply(n1,n2))
        case '/':
            print(divide(n1,n2))
        case 'x':
            break
        case _:
            print("Invalid choice")