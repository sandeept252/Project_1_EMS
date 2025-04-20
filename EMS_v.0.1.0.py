'''Project 1: EMS by Ankit Dhakal (@sandeept252)
Supervised by Neeraj Karna (@neerajkarn)

EMS (version 0.1.0) is a basic Object-Oriented Python Command Line Interface (CLI) for managinng employees database and information at a Municipality. 

This version improves on version 0.0.1 by introducing classes as modules for ease in creating, storing, and updating employee database.

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

# Employee class to store employee information
class Employee:
    def __init__(self, emp_id, name, dob, join_date, department, level, designation, status="working", exit_date=None, exit_reason=None):
        '''
        Constructor method to initialize employee object.
        Parameters:
        emp_id (str): Unique employee ID.
        name (str): Employee's name.
        dob (str): Date of birth in 'YYYY-MM-DD' format.
        join_date (str): Joining date in 'YYYY-MM-DD' format.
        department (str): Department of the employee.
        level (str): Level of the employee.
        designation (str): Designation of the employee.
        status (str): Employment status, default is "working".
        exit_date (str): Exit date in 'YYYY-MM-DD' format, default is None.
        exit_reason (str): Reason for exit, default is None.
        '''
        
        self.emp_id = emp_id
        self.name = name
        self.dob = dob
        self.join_date = join_date
        self.department = department
        self.level = level
        self.designation = designation
        self.status = status
        self.exit_date = exit_date
        self.exit_reason = exit_reason
    
    def retire(self, exit_date, exit_reason):
        '''
        Method to retire an employee.
        Parameters:
        exit_date (str): Exit date in 'YYYY-MM-DD' format.
        exit_reason (str): Reason for retirement.
        '''
        
        self.status = "retired"
        self.exit_date = exit_date
        self.exit_reason = exit_reason

    def to_dict(self):
        '''
        Method to convert employee object to dictionary.
        Returns:
        dict: Dictionary representation of employee object.
        '''
        return {
            "EMP ID": self.emp_id,
            "Name": self.name,
            "Date of Birth": self.dob,
            "Joim Date": self.join_date,
            "Department": self.department,
            "Level": self.level,
            "Designation": self.designation,
            "Status": self.status,
            "Exit Date": self.exit_date,
            "Exit Reason": self.exit_reason
        }

    def display_info(self):
        '''
        Method to display employee information.
        Returns:
        str: Formatted string of employee information.
        '''
        
        info = f"Employee ID: {self.emp_id}\nName: {self.name}\nDate of Birth: {self.dob}\nJoining Date: {self.join_date}\nDepartment: {self.department}\nLevel: {self.level}\nDesignation: {self.designation}\nStatus: {self.status}"
        if self.status == "retired":
            info += f"\nExit Date: {self.exit_date}\nExit Reason: {self.exit_reason}"
        return info

# Employee Manager class to manage employee database
class EmployeeManager:
    def __init__(self):
        '''
        Constructor method to initialize employee manager.
        Parameters:
        db_file (str): Path to the database file, default is "employee_db.csv".
        '''
        self.employees = {}

    def ask_for_date(self, prompt):
        '''
        Helper method to ask for a date input and return it in YYYY-MM-DD format
        '''
        while True:
            date_str = input(prompt)
            try:
                return datetime.strptime(date_str, "%Y-%m-%d").date()
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")

    # def load_from_excel(self):
    #     '''
    #     Method to load employees from the database file.
    #     Returns:
    #     list: List of Employee objects.
    #     '''
    #     print("Loading employees from database...\n")
    #     file_path = input("Path to the employee database file (or press ENTER to skip): ").strip()
        
    #     if file_path == "":
    #         print("No file loaded. Starting fresh.\n")
    #         return
    
    #     if not os.path.exists(file_path):
    #         print("File not found. Starting fresh.\n")
    #         return

    #     df = pd.read_excel(file_path)
    #     for _, row in df.iterrows():
    #         emp = Employee(
    #             str(row['ID']),
    #             row['Name'],
    #             pd.to_datetime(row['Date of Birth']).date(),
    #             pd.to_datetime(row['Join Date']).date(),
    #             row['Department'],
    #             row['Level'],
    #             row['Designation'],
    #             row['Status'],
    #             row['Exit Date:'],
    #             row['Exit Reason: ']
    #         )
    #         self.employees[emp.emp_id] = emp
    #     print(f"\nLoaded {len(self.employees)} entries.\n")

    def add_employee(self):
        print("Adding new employee...\n")
        emp_id = input("Employee ID: ")
        name = input("Name: ")
        dob = self.ask_for_date("Date of Birth (YYYY-MM-DD): ")    
        join_date = self.ask_for_date("Join Date (YYYY-MM-DD): ")
        department = input("Department: ")
        level = input("Level: ")
        designation = input("Designation: ")
        emp = Employee(emp_id, name, dob, join_date, department, level, designation)
        self.employees[emp_id] = emp
        print(f"Employee {emp_id} successfully added!\n")






# Main Program
print("=" * 20, "EMPLOYEE MANAGEMENT SYSTEM (PYTHON CLI VERSION 0.0.1)", "="*20)

manager = EmployeeManager()
#

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
        choice = input("Enter the Menu of your choice: ")
    except ValueError:
        print("Invalid input! Please enter a number: ")
        continue

    if choice == "1":
        manager.add_employee()

    # elif choice == "2":
    #     manager.update_employee()

    # elif choice == "3":
    #     manager.view_employee()

    # elif choice == "4":
    #     manager.view_all_employees()

    # elif choice == "5":
    #     manager.save_employee_data_to_excel()

    elif choice == "6":
        print("\nExiting...\nThank you for using our EMS.\n")
        break

    else:
        print("Invalid Choice. Try Again!\n")
