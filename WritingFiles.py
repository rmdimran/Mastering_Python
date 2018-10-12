employee_file = open ( "/home/badri/Git/Mastering_Python/Files/Employee.txt", "a" )
#appending element to the end of file
employee_file.write("Karen - Human Resources")
employee_file.write("\nKelly - Customer Service")
employee_file.close()

#override a file
# employee_file= open("/home/badri/Git/Mastering_Python/Files/Employee.txt" ,"w")
#employee_file.write("\nKelly - Customer Service")
#employee_file.close()

employee_file = open ( "/home/badri/Git/Mastering_Python/Files/Employee1.txt", "w")
employee_file.write("\n Jake - Writer")
employee_file.close()

employee_file = open ( "/home/badri/Git/Mastering_Python/Files/index.html", "w")
employee_file.write("\n <p> This is a sample page. </p>")
employee_file.close()