#   File-name     Class-name
from Class import Student

student1 = Student(int(1), "Abhishek", 3.1)
student2 = Student(int(2), "Utkarsh", 3.5)

print(student1.name, student2.name)

print(student2.on_honor_roll())