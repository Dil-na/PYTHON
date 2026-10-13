# if statement
# if  condition:
#        body of if
#        .
#        .
#        .
# if-else statement
# if condition:
#        body of if
#        .
#        .
# else:
# body of else

age = 21

# if age >= 18:
#     print('Adult')
if age>=18:
    print('Adult')
else:
    print("child")

print ("end of if")

amount = int(input("enter the total amount:"))
if amount >= 5000:
    print("free delivery available")
else:
    amount += 40
    print("free delivery not available")
print("Total payable:", amount)

# if-elif-else statement

# if condition1:
# body
# elif condition2:
# body
# elif condition3:
#      .
#      .
#      .
# else:
#     block of else

mark = int(input("Enter the mark:"))
if mark > 90:
    print("A+")
elif mark > 80:
    print("A")
elif mark > 70:
    print("B+")
elif mark > 60:
    print("B")
elif mark > 50:
    print("C+")
elif mark < 40:
    print("E")
else:
    print("Invalid mark entry")

age = 19
if age >=18:
    print("passed age requirements.")
    mark = 40
    if mark > 50 :
        print ("Admission granted")
    else:
        print("Admisssion rejected: insufficient marks.")
else:
    print("Admission rejected: insufficient age")


    day = input ('Enter the number of the day :')
    match day:
        case "1":
            print('Monday')
        case "2":
            print('Tuesday')
        case "3":
            print('Wednesday')
        case "4":
            print('Thursday')
        case "5":
            print('Friday')
        case "6":
            print('Saturday')
        case "7":
            print('Sunday')
        case _:
            print("Invalid entry")

age = int(input('Enter age:'))
match age>=18:
    case True:
        print('Adult')
    case False:
        print("Child")

day ="Wednesday"
match day:
    case "Monday" | "Tuesday" | "Wednesdsay" | "Thursday"  | "Friday":
        print("weekday")
    case "Saturday"  | "Sunday":
        print("weekend")
    case _:
         print("Invalid")

result = "Adult" if age>=18 else "child"
print(result)

# TrueExpression if codition else FalseExpression 

n = 56
even_or_odd = "Even" if n%2==0 else "odd"
print(even_or_odd)