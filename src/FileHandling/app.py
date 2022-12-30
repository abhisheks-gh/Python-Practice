

# open("employees.txt", "r")  # Opening file in read mode
# open("employees.txt", "w")  # Opening file in write mode
# open("employees.txt", "a")  # Opening file to append at the last of it
# open("employees.txt", "r+")  # Opening file in read & write mode

employee_file = open("employees.txt", "r")
print(employee_file.readable()) # True
print(employee_file.read())
print(employee_file.readline()) # reads individual line inside the file
employee_file.close()


# employee_file = open("employees.txt", "r")
# for employee_file in employee_file.readlines():
#     print(employee)

# employee_file.close()