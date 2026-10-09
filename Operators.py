# Arithmetic Operators
a = 10
b = 5
print( a + b) #addition
print( a - b) #subtraction
print( a * b) #multiplication
print( a / b) #division
print( a // b)  # floor division
print( a % b) #modulus
print( a ** 2) #exponentiation

# Assignment Operators
#  = (assign)
a+=5  #a = a+
a-=5  #a = a-5
a*=5  #a = a*5
a/=5  #a = a/5
a//=5  #a = a//5
a%=5  #a = a%5
a**=5  #a = a**5
print(a)


# Comparison Operators
print(a<b) #less than
print(a>b) #greater than
print(a<=b) #less than or equal to
print(a>=b) #greater than or equal to
print(a==b) #equal to
print(a!=b) #not equal to


# logical Operators (and, or, not)
# And operator returns True if both conditions are True, otherwise it returns False.
age = 17
has_voters_id = False
eligible_to_vote = age >= 18 and has_voters_id == True
print(eligible_to_vote) # False

# condition1             condition2         result
# True                   True               True
# True                   False              False
# False                  True               False
# False                  False              False

has_adhaar_card = True
has_driving_license = False
can_mark_voting = has_adhaar_card or has_driving_license
print(can_mark_voting) # True

# OR operator returns True if at least one of the conditions is True, otherwise it returns False.
# condition1             condition2         result
# True                   True               True
# True                   False              True
# False                  True               True
# False                  False              False

n1 = int(input("Enter a number:\t "))
n2 = int(input("Enter another number:\t "))
print(n1)
print(type(n1))
print(n1>n2)

print(bool(False))
print(bool(True))
print(bool(0))
print(bool(1))
print(bool(1000))
print(bool(-1))
print(bool("Hello"))
print(bool(""))
print(bool([]))
print(bool([1,2,3]))
print(bool("hello" and "world"))
print(bool(0 and "hello"))
print(bool([1] or "world"))