'''Project 1: EMS by Ankit Dhakal (@sandeept252)
Supervised by Neeraj Karna (@neerajkarn)

EMS (version 0.0.1) is a basic Procedural Python Command Line Interface (CLI) for managinng employees database and information at a Municipality. 
This version can be used to create, store, and update employee database.

1. Each employee has a unique ID connected to various modules.
2. Employees are classified into Working or Retired.
3. Working Employees have access to the following modules:
    i. Employee Information
    ii. Attendance
    iii. Salary, allowance, and other benefits
    iv. Performance Score
4. Retired Employees have access to the following modules:
    i. Employee Information
    ii. Pension Management
5. Each employee or *User* gets an authorized access to their personal information.
6. *User* information can be accessed and updated by *Super User*.
7. *User* and *Super User* are managed by *Admin*
''' 
import os
import pandas as pd
from datetime import datetime

# Data
employees = {}
attendance_records = {}
leave_records = {}
salary_bookings = {}
performance_scores = {}
pensions = {}

# Module 1: Employee Database -- create and update
def save_employee_data_to_excel(data, file_name="employees.xlsx"):
    folder_path = input("Folder to save the file: ")

    os.makedirs(folder_path, exist_ok=True)
    
    df = pd.DataFrame(data)

    file_path = os.path.join(folder_path, file_name)

    df.to_excel(file_path, index = False)

    print(f"File saved successfully at: {file_path}")
    
    return file_path

def add_employee():
    print("Adding new employee...\n")
    emp_id = input("Employee ID: ")
    name = input("Name: ")
    department = input("Department: ")
    dob = input("Date of Birth (YYYY-MM-DD): ")
    join_date = input("Join Date (YYYY-MM-DD): ")
    employees[emp_id] = {
            "name": name,
            "date_of_birth": dob,
            "department": department,
            "join_date": join_date,
            "status": "working",    # "working", "retired", "resigned" or "deceased" with "working" default
            "exit_date": None,      # Exit Date is None by default
            "exit_reason": None     # Exit Reason is None by default
        }
    
    print(f"Employee {emp_id} successfully added!\n")

# def update_employee():

def view_employee():
    emp_id = input("Enter Employee ID to view: ")
    if emp_id in employees:
        emp = employees[emp_id]
        print("\n=== Employee Details ===")
        for key, value in emp.items():
            print(f"{key}: {value}")
    else:
        print("Employee not found.")

def view_all_employees():
    if not employees:
        print("No employee records available.")
        return
    print("\n=== All Employees ===\n")
    print(f"{'ID':<8} {'Name':<15} {'Dept':<12} {'Status':<12}")
    for emp_id, emp in employees.items():
        print(f"{emp_id:<8} {emp['name']:<15} {emp['department']:<12} {emp['status']:<12}")

#def retire_employee(emp_id):
    #if emp_id in employees:
        #employees[emp_id]["status"]



# Main Program
print("=" * 20, "EMPLOYEE MANAGEMENT SYSTEM (PYTHON CLI VERSION 0.0.1)", "="*20)

while True:
    # Menu
    print('''Menu:
        1. Add new employee in the database
        2. Update existing database
        3. View an Employee
        4. View all Employees
        5. Save
        6. Exit
    ''')

    choice = int(input("Enter the Menu of your choice: "))

    if choice == 1:
        add_employee()

    # elif choice == 2:
    #     update_employee()

    elif choice == 3:
         view_employee()

    elif choice == 4:
        view_all_employees()

    elif choice == 5:
        save_employee_data_to_excel(employees)

    elif choice == 6:
        print("Exiting...\n Thank you for using our EMS.")
        break

    else:
        print("Invalid Choice. Try Again!\n")