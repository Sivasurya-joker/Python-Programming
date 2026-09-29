# normal mode 
def square(x):   # argument name small 'x'
    return x * x

print(square(5))

# lambda function 
square = lambda x: x * x
print(square(5))

# sorting 

# empty list create pannuvom
students = []

# student count eduthukkalam
n = int(input("Enter number of students: "))

# loop la data collect panna
for i in range(n):
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    students.append((name, age))

# sort by age
students.sort(key=lambda x: x[1])

# print result
print("\nStudents sorted by age:")
for s in students:
    print(s)
     
