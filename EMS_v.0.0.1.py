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
def load_employee_data_from_excel():
    """
    Load existing employee data from an excel file into the employees dictionary
    """
    print("Loading file...\n")

    file_path = input("Enter path to  existing employee file (or press Enter to skip): ")

    if file_path == "":
        print("No file loaded. Starting fresh.\n")
        return
    
    if not os.path.exists(file_path):
        print("File not found. Starting fresh.\n")
        return

    df = pd.read_excel(file_path)
    for _, row in df.iterrows():
        emp_id = str(row['ID'])
        employees[emp_id] = {
            "emp_id": emp_id,
            "name": row['Name'],
            "date_of_birth": row['Date of Birth'],
            "department": row['Dept'],
            "join_date": row['Join Date'],
            "status": row['Status'],
            "exit_date": row['Exit Date'],
            "exit_reason": row['Exit Reason']
        }
    print(f"\nLoaded {len(employees)} entries.\n")

def view_employee():
    """
    View employee data tagged by the Employee ID.
    """
    emp_id = input("Enter Employee ID to view: ")
    if emp_id in employees:
        emp = employees[emp_id]
        print("\n=== Employee Details ===")
        for key, value in emp.items():
            print(f"{key}: {value}")
    else:
        print("Employee not found.\n")

def view_all_employees():
    """
    View all the employee data as a table
    """
    if not employees:
        print("No employee records available.\n")
        return
    print("\n=== All Employees ===\n")
    print(f"{'ID':<8} {'Name':<15} {'Date of birth':<10} {'Dept':<12} {'Join Date':<10} {'Status':<12} {'Exit Date':<10} {'Exit Reason':<20}")
    for emp_id, emp in employees.items():
        print(f"{emp_id:<8} {emp['name']:<15} {emp['date_of_birth']:<10} {emp['department']:<12} {emp['join_date']:<10} {emp['status']:<12} {emp['exit_date']:<10} {emp['exit_reason']:<20}")

def add_employee():
    """
    Add employee data. Data of one employee can be input at a time.
    """
    print("Adding new employee...\n")
    emp_id = input("Employee ID: ")
    name = input("Name: ")
    department = input("Department: ")
    dob = input("Date of Birth (YYYY-MM-DD): ")
    join_date = input("Join Date (YYYY-MM-DD): ")
    employees[emp_id] = {"emp_id": emp_id, 
                         "name": name, 
                         "date_of_birth": dob, 
                         "department": department, 
                         "join_date": join_date, 
                         "status": "working", 
                         "exit_date": None, 
                         "exit_reason": None
                         }
    
    print(f"Employee {emp_id} successfully added!\n")

def update_employee():
    """
    Update the information of an existing employee
    """
    emp_id = input("Enter Employee ID to update: ")
    if emp_id not in employees:
        print("Employee not found.\n")
        return
    
    emp = employees[emp_id]

    print("\n=== Current Employee Details ===")
    for key, value in emp.items():
        print(f"{key}: {value}")

    print("\nWhich field do you want to update?")
    print("1. Name")
    print("2. Department")
    print("3. Date of Birth")
    print("4. Join Date")
    print("5. Status (working/retired)")
    print("6. Exit Date")
    print("7. Exit Reason")
    print("8. Cancel")

    choice = input("Enter your choice: ")

    if choice == "1":
        emp["name"] = input("Enter new name: ")
    elif choice == "2":
        emp["department"] = input("Enter new department: ")
    elif choice == "3":
        emp["date_of_birth"] = input("Enter new date of birth (YYYY-MM-DD): ")
    elif choice == "4":
        emp["join_date"] = input("Enter new join date (YYYY-MM-DD): ")
    elif choice == "5":
        emp["status"] = input("Enter new status (working/retired): ")
    elif choice == "6":
        emp["exit_date"] = input("Enter new exit date (YYYY-MM-DD): ")
    elif choice == "7":
        emp["exit_reason"] = input("Enter new exit reason: ")
    elif choice == "8":
        print("Update cancelled.\n")
        return
    else:
        print("Invalid choice.\n")
        return

    print(f"Employee {emp_id} updated successfully!\n")

def save_employee_data_to_excel():
    """
    Save employee data as an excel file
    """
    print("Saving data to database...\n")
    
    folder_path = input("Folder to save the file: ")

    os.makedirs(folder_path, exist_ok=True)
    
    file_name="employees.xlsx"

    file_path = os.path.join(folder_path, file_name)
    
    data = []
    for emp_id, emp in employees.items():
        record = {"ID": emp_id,
            "Name": emp["name"],
            "Date of Birth": emp["date_of_birth"],
            "Dept": emp["department"],
            "Join Date":emp["join_date"],
            "Status": emp["status"],
            "Exit Date": emp["exit_date"],
            "Exit Reason": emp["exit_reason"]}
        data.append(record)

    # Create a DataFrame from the given fields
    df = pd.DataFrame(data, columns=["ID", "Name", "Date of Birth", "Dept", "Join Date", "Status", "Exit Date", "Exit Reason"])


    df.to_excel(file_path, index=False)

    print(f"File saved successfully at: {file_path}\n")
#def retire_employee(emp_id):
    #if emp_id in employees:
        #employees[emp_id]["status"]



# Main Program
print("=" * 20, "EMPLOYEE MANAGEMENT SYSTEM (PYTHON CLI VERSION 0.0.1)", "="*20)

load_employee_data_from_excel()

while True:
    # Menu
    print('''Menu:
        1. Add new employee in the database
        2. Update existing employee data 
        3. View an Employee
        4. View all Employees
        5. Save
        6. Exit
    ''')

    try:
        choice = int(input("Enter the Menu of your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number: ")
        continue

    if choice == 1:
        add_employee()

    elif choice == 2:
        update_employee()

    elif choice == 3:
         view_employee()

    elif choice == 4:
        view_all_employees()

    elif choice == 5:
        save_employee_data_to_excel()

    elif choice == 6:
        print("\nExiting...\nThank you for using our EMS.\n")
        break

    else:
        print("Invalid Choice. Try Again!\n")