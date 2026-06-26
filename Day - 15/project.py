import json
import os
from datetime import datetime

class AttendanceSystem:
    def __init__(self, filename="attendance_data.json"):
        self.filename = filename
        self.data = self.load_data()
    def load_data(self):                                       # loads attendance data from the file
        if not os.path.exists(self.filename):
            return {}
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error: Data file is corrupted. Starting fresh.")
            return {}
    def save_data(self):                                            # saves live data to the JSON file
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=4)
    def add_student(self, class_name, subject, roll_no, name):           # adds a student to a specific class and subject
        if class_name not in self.data:
            self.data[class_name] = {}
        if subject not in self.data[class_name]:
            self.data[class_name][subject] = {}
        if roll_no in self.data[class_name][subject]:
            print(f"Student with Roll No {roll_no} already exists.")
        else:
            self.data[class_name][subject][roll_no] = {"name": name, "attendance_records": {}}
            self.save_data()
            print(f"Student '{name}' added successfully to {class_name} - {subject}.")
    def mark_attendance(self, class_name, subject, roll_no, date, is_present):         # marks attendance for a student on a specific date
        try:
            student = self.data[class_name][subject][roll_no]
            student["attendance_records"][date] = is_present
            self.save_data()
            status = "Present" if is_present else "Absent"
            print(f"Attendance marked: {student['name']} is {status} on {date}.")
        except KeyError:
            print("Error: Class, Subject, or Roll No not found.")
    def generate_overall_report(self, class_name, subject):                    # generates an overall percentage report for all dates
        try:
            students = self.data[class_name][subject]
            print(f"\n--- Overall Report: {class_name} | {subject} ---")
            print(f"{'Roll No':<10} | {'Name':<15} | {'Total':<7} | {'Attended':<10} | {'Percentage':<12} | {'Warning'}")
            print("-" * 75)
            
            for roll_no, data in students.items():
                records = data["attendance_records"]
                total = len(records)
                attended = sum(1 for status in records.values() if status is True)
                percentage = (attended / total * 100) if total > 0 else 0.0
                warning = "LOW ATTENDANCE" if percentage < 75.0 and total > 0 else "OK"
                print(f"{roll_no:<10} | {data['name']:<15} | {total:<7} | {attended:<10} | {percentage:<11.2f}% | {warning}")
            print("-" * 75)
        except KeyError:
            print("Error: No records found for this Class and Subject.")

    def generate_daily_report(self, class_name, subject, target_date):                 # generates a report on a specific date
        try:
            students = self.data[class_name][subject]
            print(f"\n--- Daily Report: {class_name} | {subject} | Date: {target_date} ---")
            print(f"{'Roll No':<10} | {'Name':<15} | {'Status'}")
            print("-" * 45)
            found_records = False
            for roll_no, data in students.items():
                records = data["attendance_records"]
                if target_date in records:
                    found_records = True
                    status = "Present" if records[target_date] else "Absent"
                    print(f"{roll_no:<10} | {data['name']:<15} | {status}")
            if not found_records:
                print(f"No attendance was recorded on {target_date}.")
            print("-" * 45)
        except KeyError:
            print("Error: No records found for this Class and Subject.")

def get_date_input():                                                                  # function to get a date or default to today
    date_str = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
    if not date_str:
        return datetime.today().strftime('%Y-%m-%d')
    return date_str

def main():
    system = AttendanceSystem()
    while True:
        print("\n=== Student Attendance Management System ===")
        print("1. Add a Student")
        print("2. Mark Attendance")
        print("3. Generate Report")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        try:
            if choice == '1':
                c_name = input("Enter Class Name: ").strip().upper()
                roll = input("Enter Roll No: ").strip()
                name = input("Enter Student Name: ").strip().title()
                system.add_student(c_name, sub, roll, name)
                
            elif choice == '2':
                c_name = input("Enter Class Name: ").strip().upper()
                sub = input("Enter Subject Name: ").strip().title()
                roll = input("Enter Roll No: ").strip()
                date = get_date_input()
                status = input("Present? (y/n): ").strip().lower()
                
                if status not in ['y', 'n']:
                    raise ValueError(" use 'y' or 'n' ")
                system.mark_attendance(c_name, sub, roll, date, status == 'y')
                
            elif choice == '3':
                c_name = input("Enter Class Name: ").strip().upper()
                sub = input("Enter Subject Name: ").strip().title()
                print("\nReport Types:")
                print("A. Overall Percentage Report")
                print("B. Specific Date Report")
                rep_type = input("Choose (A/B): ").strip().upper()
                
                if rep_type == 'A':
                    system.generate_overall_report(c_name, sub)
                elif rep_type == 'B':
                    target_date = input("Enter the date to check (YYYY-MM-DD): ").strip()
                    system.generate_daily_report(c_name, sub, target_date)
                else:
                    print("Invalid report type selected.")
                
            elif choice == '4':
                print("Saving data and exiting system. Goodbye!")
                break
            else:
                print("Invalid choice.")
                
        except ValueError as e:
            print(f"Input Error: {e}")

if __name__ == "__main__":
    main()
