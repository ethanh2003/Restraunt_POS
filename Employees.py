from ast import Break
from tokenize import Double
from unicodedata import decimal
import mysql.connector


from tkinter import *


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
    def newEmployee():
        newEmp = (id, fName, lName, pin, payRate, accessLevel, jobTitle)
        if(check_employee(id) == True):
            top.window("Employee aready exists\nTry Again\n")
        else:
            sql = 'insert into employeedata values(%s,%s,%s,%s,%s,%s,%s)'
            c = con.cursor()
    
            # Executing the SQL Query
            c.execute(sql, newEmp)
    
            # commit() method to make changes in the table
            con.commit()
            print("Employee Added Successfully ")
    top = Tk()
    L1 = Label(top, text = "New User id").grid(row=0,column=0)
    idE = Entry(top, bd = 5).grid(row=0,column=1)
    L2 = Label(top, text = "First Name").grid(row=1,column=0)
    fNameE = Entry(top, bd = 5).grid(row=1,column=1)
    L3 = Label(top, text = "Last Name").grid(row=2,column=0)
    lNameE = Entry(top, bd = 5).grid(row=2,column=1)
    L4 = Label(top, text = "Pin").grid(row=3,column=0)
    pinE = Entry(top, bd = 5).grid(row=3,column=1)
    L4 = Label(top, text = "payRate").grid(row=4,column=0)
    payRateE = Entry(top, bd = 5).grid(row=4,column=1)
    L5 = Label(top, text = "Access Level").grid(row=5,column=0)
    accessLevelE = Entry(top, bd = 5).grid(row=5,column=1)
    L5 = Label(top, text = "Job Title").grid(row=6,column=0)
    jobTitleE = Entry(top, bd = 5).grid(row=6,column=1)
    btn = Button(top ,text="Submit", command= newEmployee).grid(row=7,column=1)
    id=int(idE.get())
    fName=fNameE.get()
    lName=lNameE.get()
    pin=int(pinE.get())
    payRate=decimal(payRateE.get())
    accessLevel=int(accessLevelE.get())
    jobTitle=jobTitleE.get()
    
    
        
def deleteEmployee():

    id = input("Enter Employee Id : ")
 
    # Checking if Employee with given Id
    # Exist or Not
    if(check_employee(id) == False):
        print("Employee does not  exists\nTry Again\n")
        
     
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
        
def editEmployee():
    id = int(input("Enter Employee Id"))
 
    # Checking if Employee with given Id
    # Exist or Not
    if(check_employee(id) == False):
        print("Employee does not  exists\nTry Again\n")
        
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
    


top = Tk()
B = Button(top, text = "Add Employee", command = createEmployee)
B.place(x = 50,y = 50)
top.mainloop()