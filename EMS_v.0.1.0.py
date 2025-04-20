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
            "emp_id": self.emp_id,
            "name": self.name,
            "dob": self.dob,
            "join_date": self.join_date,
            "department": self.department,
            "level": self.level,
            "designation": self.designation,
            "status": self.status,
            "exit_date": self.exit_date,
            "exit_reason": self.exit_reason
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
    def __init__(self, db_file="employees.xlsx"):
        '''
        Constructor method to initialize employee manager.
        Parameters:
        db_file (str): Path to the database file, default is "employee_db.csv".
        '''
        
        self.db_file = db_file
        self.employees = self.load_employees()

    def load_employees(self):
        '''
        Method to load employees from the database file.
        Returns:
        list: List of Employee objects.
        '''
        print("Loading employees from database...\n")
        file_path = input("Path to the employee database file (or press ENTER to skip): ").strip()
        
        if file_path == "":
            print("No file loaded. Starting fresh.\n")
            return
    
        if not os.path.exists(file_path):
            print("File not found. Starting fresh.\n")
            return

        if os.path.exists(self.db_file):
            df = pd.read_excel(self.db_file)
            employees = {}
            for _, row in df.iterrows():
                emp = Employee(row['emp_id'], row['name'], row['dob'], row['join_date'], row['department'], row['level'], row['designation'], row['status'], row['exit_date'], row['exit_reason'])
                employees.append(emp)
            return employees
        else:
            return []