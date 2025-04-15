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

# Data
employees = {}
attendance_records = {}
leave_records = {}
salary_bookings = {}
performance_scores = {}
pensions = {}

# Module 1: Employee Database -- create and update
def add_employee(emp_id, name, age, department, join_date, status):
    employees[emp_id] = {
        "name": name,
        "age": age,
        "department": department,
        "join_date": join_date,
        "status": "working"    # "working", "retired", "resigned" or "deceased" with "working" default
    }

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

    choice = input("Enter your choice: ")

    if choice == 1:
        add_employee()

    elif choice == 2:
        update_employee()

    elif choice == 3:
        view_employee()

    elif choice == 4:
        view_all_employees()

    elif choice == 5:
        save_to_database()

    elif choice == 6:
        print("Exiting... Thank you for using our EMS.")
        break

    else:
        print("Invalid Choice. Try Again!")