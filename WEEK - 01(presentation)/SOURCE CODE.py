# STUDENT ATTENDANCE MANAGEMENT SYSTEM

import sqlite3
import os
import csv
from datetime import datetime

class AttendanceSystem:
    def __init__(self, db_name="attendance.db"):
        # Resolves the absolute path of the current script to prevent context execution errors.
        # This ensures the .db file is always generated in the project directory, regardless of 
        # where the terminal/shell was executed from.
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(base_dir, db_name)
        self.conn = sqlite3.connect(self.db_path)
        
        # SQLite disables foreign key constraints by default for backward compatibility.
        # We explicitly enable it via PRAGMA to allow cascading deletes across relational tables.
        self.conn.execute("PRAGMA foreign_keys = ON")
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        
        # Students Table: Uses a Composite Primary Key (roll_no, class_name, subject).
        # This allows the same roll number to exist across different classes/subjects without conflict.
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                roll_no TEXT,
                name TEXT,
                class_name TEXT,
                subject TEXT,
                PRIMARY KEY (roll_no, class_name, subject)
            )
        ''')
        
        # Attendance Table: Maintains relational integrity with the students table.
        # ON UPDATE CASCADE ON DELETE CASCADE ensures orphaned records don't bloat the DB; 
        # if a student drops a class, their attendance history is automatically purged.
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS attendance (
                roll_no TEXT,
                class_name TEXT,
                subject TEXT,
                date TEXT,
                status INTEGER,
                PRIMARY KEY (roll_no, class_name, subject, date),
                FOREIGN KEY (roll_no, class_name, subject) 
                REFERENCES students(roll_no, class_name, subject) 
                ON UPDATE CASCADE ON DELETE CASCADE
            )
        ''')
        self.conn.commit()

    def add_student(self, class_name, subject, roll_no, name):
        cursor = self.conn.cursor()
        try:
            # Executes a DML insert. If the composite key already exists, SQLite throws an IntegrityError,
            # which we catch to prevent the application from crashing.
            cursor.execute('''
                INSERT INTO students (roll_no, name, class_name, subject)
                VALUES (?, ?, ?, ?)
            ''', (roll_no, name, class_name, subject))
            self.conn.commit()
            print(f"Success: Student '{name}' (Roll: {roll_no}) added to {class_name} - {subject}.")
        except sqlite3.IntegrityError:
            print(f"Error: Roll No {roll_no} already exists in {class_name} for {subject}.")

    def remove_student(self, class_name, subject, roll_no):
        cursor = self.conn.cursor()
        # Executes deletion. Because PRAGMA foreign_keys = ON, this also wipes linked attendance records.
        cursor.execute('DELETE FROM students WHERE class_name=? AND subject=? AND roll_no=?', (class_name, subject, roll_no))
        
        # cursor.rowcount verifies if a mutation actually occurred. 0 means the query executed but found no matches.
        if cursor.rowcount > 0:
            self.conn.commit()
            print(f"Success: Student {roll_no} has been removed from {class_name} - {subject}.")
        else:
            print(f"Error: Could not find student {roll_no} in {class_name} - {subject}.")

    def mark_attendance_batch(self, class_name, subject, date):
        cursor = self.conn.cursor()
        cursor.execute('SELECT roll_no, name FROM students WHERE class_name = ? AND subject = ?', (class_name, subject))
        students = cursor.fetchall()
        
        if not students:
            print(f"Error: No students found in {class_name} for {subject}. Please add students first.")
            return

        print(f"\nMarking Attendance for {class_name} - {subject} on {date}")
        print(f"Total students registered: {len(students)}")
        print("Enter the Roll Numbers of ABSENT students, separated by commas (e.g., 101, 104).")
        absent_input = input("Leave blank and press Enter if EVERYONE is present: ").strip()
        
        # Normalizes the comma-separated string into a clean list of roll numbers.
        absent_rolls = [r.strip() for r in absent_input.split(',')] if absent_input else []
        
        for roll_no, name in students:
            # Evaluates boolean status to integers (SQLite lacks a native boolean datatype)
            status = 0 if roll_no in absent_rolls else 1
            
            # REPLACE INTO acts as an UPSERT operation in SQLite. 
            # If the user re-marks attendance for an existing date, it overwrites the row instead of crashing.
            cursor.execute('''
                REPLACE INTO attendance (roll_no, class_name, subject, date, status)
                VALUES (?, ?, ?, ?, ?)
            ''', (roll_no, class_name, subject, date, status))
            
        self.conn.commit()
        print(f"\nSuccess: Attendance saved for {len(students)} students.")

    def generate_overall_report(self, class_name, subject):
        cursor = self.conn.cursor()
        # Uses a LEFT JOIN to ensure students with 0 total attendance days still appear in the report.
        # Aggregation functions (COUNT, SUM) efficiently crunch the historical data directly inside the DB engine.
        query = '''
            SELECT s.roll_no, s.name, COUNT(a.date) as total_days, SUM(a.status) as attended_days
            FROM students s
            LEFT JOIN attendance a ON s.roll_no = a.roll_no AND s.class_name = a.class_name AND s.subject = a.subject
            WHERE s.class_name = ? AND s.subject = ?
            GROUP BY s.roll_no
        '''
        cursor.execute(query, (class_name, subject))
        records = cursor.fetchall()

        if not records:
            print("Error: No records found for this Class and Subject.")
            return

        print("\n" + "-" * 75)
        print(f"      Overall Report: {class_name} | {subject}")
        print("-" * 75)
        print(f"{'Roll No':<10} | {'Name':<15} | {'Total':<7} | {'Attended':<10} | {'Percentage':<12} | {'Warning'}")
        print("-" * 75)
        
        report_data = [] # Buffer for potential CSV export
        for roll_no, name, total_days, attended_days in records:
            # SQL COUNT/SUM might return None for LEFT JOINs with no matches, so we fallback to 0.
            total = total_days or 0
            attended = attended_days or 0
            percentage = (attended / total * 100) if total > 0 else 0.0
            warning = "LOW ATTENDANCE" if percentage < 75.0 and total > 0 else "OK"
            
            print(f"{roll_no:<10} | {name:<15} | {total:<7} | {attended:<10} | {percentage:<11.2f}% | {warning}")
            report_data.append([roll_no, name, total, attended, f"{percentage:.2f}%", warning])  
        print("-" * 75)
        
        # CSV Export Logic: Implements file I/O using 'newline=""' to prevent blank line injection on Windows systems.
        if input("\nDo you want to export this report to a CSV file? (y/n): ").strip().lower() == 'y':
            filename = f"{class_name}_{subject}_Report.csv"
            export_path = os.path.join(os.path.dirname(self.db_path), filename)
            with open(export_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Roll No', 'Name', 'Total Days', 'Attended Days', 'Percentage', 'Status'])
                writer.writerows(report_data)
            print(f"Success: Report exported to {export_path}")

    def generate_daily_report(self, class_name, subject, target_date):
        cursor = self.conn.cursor()
        # Standard INNER JOIN since we only care about exact matches for the targeted date.
        query = '''
            SELECT s.roll_no, s.name, a.status 
            FROM students s
            JOIN attendance a ON s.roll_no = a.roll_no AND s.class_name = a.class_name AND s.subject = a.subject
            WHERE s.class_name = ? AND s.subject = ? AND a.date = ?
        '''
        cursor.execute(query, (class_name, subject, target_date))
        records = cursor.fetchall()

        if not records:
            print(f"Error: No attendance was recorded on {target_date} for {class_name} - {subject}.")
            return

        print("\n" + "-" * 45)
        print(f"      Daily Report: {class_name} | {subject} | Date: {target_date}")
        print("-" * 45)
        print(f"{'Roll No':<10} | {'Name':<15} | {'Status'}")
        print("-" * 45)
        for roll_no, name, status in records:
            status_text = "Present" if status == 1 else "Absent"
            print(f"{roll_no:<10} | {name:<15} | {status_text}")
        print("-" * 45)

    def view_database_summary(self):
        cursor = self.conn.cursor()
        # Global grouping query to generate a complete overview of the current DB state.
        query = '''
            SELECT s.class_name, s.subject, s.roll_no, s.name, COUNT(a.date), SUM(a.status)
            FROM students s
            LEFT JOIN attendance a ON s.roll_no = a.roll_no AND s.class_name = a.class_name AND s.subject = a.subject
            GROUP BY s.class_name, s.subject, s.roll_no
            ORDER BY s.class_name, s.subject, s.roll_no
        '''
        cursor.execute(query)
        records = cursor.fetchall()

        if not records:
            print("\n[INFO] The database is currently empty. No students are registered yet.")
            return

        print("\n" + "-" * 85)
        print(" " * 18 +" Database Summary: All Classes, Subjects & Students" + " " * 18)
        print("-" * 85)
        print(f"{'Class':<10} | {'Subject':<15} | {'Roll No':<10} | {'Name':<15} | {'Attendance %':<15} | {'Status'}")
        print("-" * 85)
        for c_name, sub, roll_no, name, total_days, attended_days in records:
            total = total_days or 0
            attended = attended_days or 0
            percentage = (attended / total * 100) if total > 0 else 0.0
            
            if total == 0: warning = "NO DATA"
            elif percentage < 75.0: warning = "LOW (<75%)"
            else: warning = "OK"
                
            print(f"{c_name:<10} | {sub:<15} | {roll_no:<10} | {name:<15} | {percentage:<14.2f}% | {warning}")
        print("-" * 85)

    def close(self):
        self.conn.close()

def get_date_input():
    # Employs an infinite while loop that traps the user until strict validation passes.
    # Uses datetime.strptime to syntactically parse the date string against the ISO-8601 subset.
    while True:
        date_str = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
        if not date_str:
            return datetime.today().strftime('%Y-%m-%d')
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return date_str
        except ValueError:
            print("Invalid date format! Please strictly use YYYY-MM-DD (e.g., 2024-10-25).")

def main():
    system = AttendanceSystem()
    print(f"\n[INFO] Database is locked to: {system.db_path}")
    
    # Global exception wrapper for the CLI loop to prevent catastrophic stack traces from breaking the UX.
    try:
        while True:
            print("\n" + "=" * 60)
            print("|           Student Attendance Management System           |")
            print("=" * 60)
            print("| 1. View Database Summary (Classes, Subjects & Students)  |")
            print("| 2. Add a New Student                                     |")
            print("| 3. Remove a Student                                      |")
            print("| 4. Mark Attendance                                       |")
            print("| 5. Generate Report                                       |")
            print("| 6. Exit                                                  |")
            print("=" * 60)
            choice = input("Enter your choice (1-6): ")
            
            # Input normalizations (.strip(), .upper(), .title()) are applied aggressively to 
            # standardize the data before it touches the SQL engine, preventing duplicate keys 
            # differing only by casing/whitespace.
            if choice == '1':
                system.view_database_summary()
                
            elif choice == '2':
                c_name = input("Enter Class Name: ").strip().upper()
                sub = input("Enter Subject Name: ").strip().title()
                roll = input("Enter Roll No: ").strip()
                name = input("Enter Student Name: ").strip().title()
                system.add_student(c_name, sub, roll, name)
                
            elif choice == '3':
                c_name = input("Enter Class Name: ").strip().upper()
                sub = input("Enter Subject Name: ").strip().title()
                roll = input("Enter Roll No of Student to Remove: ").strip()
                system.remove_student(c_name, sub, roll)
                
            elif choice == '4':
                c_name = input("Enter Class Name: ").strip().upper()
                sub = input("Enter Subject Name: ").strip().title()
                date = get_date_input()
                system.mark_attendance_batch(c_name, sub, date)
                
            elif choice == '5':
                c_name = input("Enter Class Name: ").strip().upper()
                sub = input("Enter Subject Name: ").strip().title()
                print("\nReport Types:\nA. Overall Percentage Report\nB. Specific Date Report")
                rep_type = input("Choose (A/B): ").strip().upper()
                
                if rep_type == 'A':
                    system.generate_overall_report(c_name, sub)
                elif rep_type == 'B':
                    target_date = get_date_input()
                    system.generate_daily_report(c_name, sub, target_date)
                else:
                    print("Invalid report type selected.")
                    
            elif choice == '6':
                print("Closing database connection and exiting system. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 6.")
                
    except KeyboardInterrupt:
        # Catches CTRL+C to ensure safe shutdown and database lock release.
        print("\nProgram interrupted manually. Exiting safely.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # The finally block guarantees the DB connection is closed, preventing lockups and memory leaks.
        system.close()

if __name__ == "__main__":
    main()



'''
System Flow Chart:-

Imports
    │
    ▼
AttendanceSystem Class
    │
    ├── __init__()
    │       │
    │       ├── Connect Database
    │       └── Create Tables
    │
    ├── add_student()
    ├── remove_student()
    ├── mark_attendance_batch()
    ├── generate_overall_report()
    ├── generate_daily_report()
    ├── view_database_summary()
    └── close()
            │
            ▼
Utility Function
(get_date_input)
            │
            ▼
main()
            │
            ▼
Infinite Menu Loop
            │
            ▼
User Chooses Option
            │
            ▼
Required Function Executes
            │
            ▼
Database Reads/Writes Data
            │
            ▼
Display Output
            │
            ▼
Return to Menu
            │
            ▼
Exit
            │
            ▼
Database Closes




Inside `main()`, an object of the `AttendanceSystem` class is created, automatically executing the `__init__()` constructor.
The constructor initializes the project, establishes the SQLite database connection, enables foreign keys, and creates the required 
tables if they do not already exist.

The database contains two tables:

* students – stores Roll Number, Name, Class, and Subject.
* attendance – stores attendance records with Date and Status.

    |--> These tables are linked through a foreign key with **ON DELETE CASCADE**, ensuring that attendance records are automatically 
         removed when a student is deleted.
    |--> After initialization, the program enters a continuous menu loop where users can perform different operations until 
         they choose to exit.
            (1) VIEW DATABASE SUMMARY: Displays all students along with their attendance percentage and status (OK, LOW, or NO DATA).
            (2) ADD STUDENT: Accepts student details, validates the input and inserts the record into the database while preventing duplicate roll numbers.
            (3) REMOVE STUDENT: Deletes a student and automatically removes all associated attendance records.
            (4) MARK ATTENDANCE: Accepts a class, subject, and date(defaulting to today's date if left blank). Instead of marking 
                                 every student individually, the user enters only the roll numbers of absent students. Remaining 
                                 students are automatically marked present. Attendance is stored using SQLite's `REPLACE INTO` statement, 
                                 allowing updates for existing records.
            (5) GENERATE REPORTS: Users can generate two types of reports with option [A] & [B]
                --> [A] Overall Report: Calculates attendance percentage using SQL aggregation functions, highlights students with 
                                        attendance below 75%, and optionally exports the report as a CSV file.
                --> [B] Daily Report: Displays attendance for a selected date, showing whether each student was Present or Absent.

The helper function `get_date_input()` validates the date format (`YYYY-MM-DD`) and repeatedly prompts the user until 
a valid date is entered. If no date is provided, the current date is used.
'''
