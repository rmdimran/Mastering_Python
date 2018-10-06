employee_file = open('/home/badri/Git/Python4HoursCourse/Files/Employee.txt', "r")
print(employee_file.readable())
print(employee_file.readline())

employee_file.close()