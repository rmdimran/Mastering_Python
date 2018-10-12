employee_file = open ( '/home/badri/Git/Mastering_Python/Files/Employee.txt', "r" )  # read mode

print(employee_file.readable())
print(employee_file.readline()) #read single line
print(employee_file.readlines()) #read all lines
print(employee_file.readlines()[2]) #read particular element of files

#using for loop to print elements of a file
for employee in employee_file.readlines():
 print (employee)

employee_file.close()
