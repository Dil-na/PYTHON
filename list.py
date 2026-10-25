numbers = [78,34,56,12,3,98,75,64]
print(numbers)
print(type(numbers))
print(len(numbers))
print(numbers[6])
print(numbers[-1])
print(numbers[1:6])
print(numbers[-7:-2])
print(numbers[:-2])
print(numbers[4:])
print(numbers[::2])
print(numbers[::-1])
print(numbers[::-2])
print(numbers[0])
numbers[4]=100
numbers.append(83)
numbers.append(8)
numbers.insert(5,23)
numbers.extend("hai")
numbers.extend([23,21,43])

print(numbers)
# even_count = 0
# for n in numbers:
#     if n % 2 == 0:
#         even_count += 1

# print(even_count)

# numbers.pop()
# numbers.remove(100)
# del numbers[7]
# numbers.clear()

l2 =[]
l3 = list(numbers)
print(numbers)
print(l3)  
print(l3 is numbers)

print(numbers.count(77))
print(numbers.index(100))
print(22 in numbers)
print(22 not in numbers)

l4 = numbers.copy()

l4[1]="dilna"
print(l4)
print(numbers)
print(l4 is numbers)
# numbers.sort(reverse=True)
numbers.reverse()
print(numbers)

l5 = [[12,12,13],[78,74,20],[100,200,366]]
print(l5[1][2])

l6 = l5.copy()    #shallow copy
l6[1][2] =555
l6[2]=56
print(l5)
print(l6)


# for x in l5:
#     for  in x:
#         print(n)
