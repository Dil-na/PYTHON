n=5
# def square(x):
#     return x*x
# print(square(n))
# print(square(5))
# print(square(7))
# print(square(9))


# square = lambda x: x*x
# print(square(n))   
# print(square(5))
# print(square(7))
# print(square(9))

def type_of_number(n):
    if n>0:
        return "Positive"
    elif n<0:
        return "Negative"
    else:
        return "Zero"

# TrueExpession if condition else FalseExpression
check_type = lambda n: "Positive" if n>0 else ("Negative" if n<0 else "Zero")
print(check_type(5))
print(check_type(-5))
print(check_type(0))

from functools import reduce
l1 = [1,2,3,4,5]
squared_numbers = list(map(lambda x: x*x, l1))
even_numbers = filter(lambda x: x%2==0, l1)
result = reduce(lambda x,y: x+y, l1)
print(squared_numbers)
print(list(even_numbers))
print(result)
