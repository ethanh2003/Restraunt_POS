import mysql.connector
con = mysql.connector.connect(
    host="localhost", user="root", password="root", database="Employees")

def check_employee(employee_id):
 
    # Query to select all Rows f
    # rom employee Table
    sql = 'select * from empd where id=%s'
 
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
        sql = 'insert into empd values(%s,%s,%s,%s,%s,%s,%s)'
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
        sql = 'update empd set salary=%s where id=%s'
        d = (t, Id)
 
        # Executing the SQL Query
        c.execute(sql, d)
 
        # commit() method to make changes in the table
        con.commit()
        print("Employee Promoted")
        menu()
    