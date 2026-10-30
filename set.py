# student = {"dilna","vicky","ashin"}
# n = set()
# print(type(n))
# student.add("Dino")
# student.remove("dilna") 
# # student.remove("micky")
# student.discard("vicky")
# student.pop()
# student.clear()
# student.remove("ashin")
# student.add("ashna")
# print(student)
# print(len(student))
# for student in student:
#     print(student)

# print(set(["python","mern","python","ds","ds","python"]))
# print({"Harish","a",1,True,0,False,45,-89})

# movie_set_1 = {"Jailer","kilukkam","CLD 'Moosa","KGF","vettam"}
# movie_set_2= {"vettom","KGF","drishyam","obsession","parava"}

# print(movie_set_1.union(movie_set_2))
# print(movie_set_1 | movie_set_2)
# print(movie_set_1.intersection(movie_set_2))
# print(movie_set_1 & movie_set_2)
# print(movie_set_1.difference(movie_set_2))
# print(movie_set_1 - movie_set_2)
# print(movie_set_2 - movie_set_1)
# print(movie_set_1.symmetric_difference (movie_set_2))
# print(movie_set_1 ^ movie_set_2)
# print(movie_set_1.update(movie_set_2))
# print(movie_set_1.intersection_update(movie_set_2))
# print(movie_set_1.difference_update(movie_set_2))
# print(movie_set_1.symmetric_difference_update(movie_set_2))
# print(movie_set_1)

numbers = {1,2,45,78,93,65,10.2}
even_numbers = {2,78,96,10,2}

print(numbers.issuperset(even_numbers))
print(even_numbers.issubset(numbers))
print(numbers.isdisjoint(even_numbers))
print({1,5,7}.isdisjoint({2,8,10}))
