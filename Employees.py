from ast import Break
import mysql.connector


from tkinter import *
top = Tk()
menu()
top.mainloop()

con = mysql.connector.connect(
    host="localhost", user="root", password="root", database="Employees")

def check_employee(employee_id):
 
    # Query to select all Rows f
    # rom employee Table
    sql = 'select * from employeedata where id=%s'
 
    # making cursor buffered to make
    # rowcount method work properly
    c = con.cursor(buffered=True)
    data = (employee_id,)
 
    # Executing the SQL Query
    c.execute(sql, data)
 
    # rowcount method to find
    # number of rows with given values
    r = c.rowcount
     
    if r == 1:
        return True
    else:
        return False
    
def createEmployee(): 
    id = tk.Text(frame,"Enter Employee ID",
                    height = 5,
                    width = 20)
    
    id.pack()
    
         # Button Creation
    Submit = tk.Button(frame,
                            text = "Submit", 
                            command = printInput)
    printButton.pack()
    
    id = input("Enter Employee Id : ")
 
    # Checking if Employee with given Id
    # Already Exist or Not
    if(check_employee(id) == True):
        print("Employee aready exists\nTry Again\n")
        menu()
     
    else:
        fName = input("Enter Employee First Name : ")
        lName = input("Enter Employee Last Name : ")
        pin = input("Enter Employee Pin : ")
        payRate = input("Enter Employee payRate : ")
        accessLevel = input("Enter Employee Access Level: ")
        jobTitle = input("Enter Job Title")
        newEmp = (id, fName, lName, pin, payRate, accessLevel, jobTitle)
 
        # Inserting Employee details in the Employee
        # Table
        sql = 'insert into employeedata values(%s,%s,%s,%s,%s,%s,%s)'
        c = con.cursor()
 
        # Executing the SQL Query
        c.execute(sql, newEmp)
 
        # commit() method to make changes in the table
        con.commit()
        print("Employee Added Successfully ")
        menu()
def deleteEmployee():

    id = input("Enter Employee Id : ")
 
    # Checking if Employee with given Id
    # Exist or Not
    if(check_employee(id) == False):
        print("Employee does not  exists\nTry Again\n")
        menu()
     
    else:
         
        # Query to Delete Employee from Table
        sql = 'delete from employeedata where id=%s'
        data = (id,)
        c = con.cursor()
 
        # Executing the SQL Query
        c.execute(sql, data)
 
        # commit() method to make changes in
        # the table
        con.commit()
        print("Employee Removed")
        menu()
def editEmployee():
    id = int(input("Enter Employee Id"))
 
    # Checking if Employee with given Id
    # Exist or Not
    if(check_employee(id) == False):
        print("Employee does not  exists\nTry Again\n")
        menu()
    else:
        #pin accessLevel jobTitle payRate
        selection = int(input("Select 1 to edit pin /n Select 2 to edit accessLevel /n Select 3 to edit job title /n Select 4 to edit pay rate"))
        
        Amount = int(input("Enter increase in Salary"))
 #TODO: Impliment Selection Option and change sql selection
        # Query to Fetch Salary of Employee with
        # given Id
        sql = 'select salary from employeedata where id=%s'
        data = (id,)
        c = con.cursor()
 
        # Executing the SQL Query
        c.execute(sql, data)
 
        # Fetching Salary of Employee with given Id
        r = c.fetchone()
        t = r[0]+Amount
 
        # Query to Update Salary of Employee with
        # given Id
        sql = 'update employeedata set salary=%s where id=%s'
        d = (t, id)
 
        # Executing the SQL Query
        c.execute(sql, d)
 
        # commit() method to make changes in the table
        con.commit()
        print("Employee Promoted")
        menu()
def Display_Employees():
     
    # query to select all rows from
    # Employee Table
    sql = 'select * from employeedata'
    c = con.cursor()
     
    # Executing the SQL Query
    c.execute(sql)
     
    # Fetching all details of all the
    # Employees
    r = c.fetchall()
    for i in r:
        print("Employee Id : ", i[0])
        print("Employee Name : ", i[1], " " , i[2])
        print("Employee payRate : ", i[6])
        print("Employee access level : ", i[4])
        print("Employee Job Title : ", i[5])
        print("-----------------------------\
        -------------------------------------\
        -----------------------------------")
    menu()
def menu():
    B = Button(top, text = "Add Employee", command = createEmployee())


