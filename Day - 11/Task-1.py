headers = ['Roll_No', 'Name', 'Math', 'Science', 'English', 'History']
students_data = [
    [1, 'Alice', 85, 88, 90, 82],
    [2, 'Bob', 92, 95, 85, 88],
    [3, 'Charlie', 78, 82, 88, 75],
    [4, 'David', 90, 85, 92, 89],
    [5, 'Eva', 88, 91, 84, 90],
    [6, 'Frank', 76, 79, 80, 72],
    [7, 'Grace', 95, 94, 96, 91],
    [8, 'Hannah', 89, 88, 91, 85],
    [9, 'Ian', 82, 85, 86, 80],
    [10, 'Jack', 91, 92, 89, 93]
]

file_path = 'student.csv'
with open(file_path, mode='w') as file:
    file.write(','.join(headers) + '\n')
    for row in students_data:
        row_string = ','.join(str(item) for item in row)
        file.write(row_string + '\n')

highest_score = -1
top_student_name = ""
total_class_score = 0
num_students = 0
print(f"{'Roll No':<8} | {'Name':<10} | {'Math':<5} | {'Science':<7} | {'English':<7} | {'History':<7} | {'Total':<5} | {'Average':<7}")
print("-" * 80)

with open(file_path, mode='r') as file:
    lines = file.readlines()
    for line in lines[1:]:
        clean_line = line.strip()
        columns = clean_line.split(',')
        roll_no = columns[0]
        name = columns[1]
        
        math = int(columns[2])
        science = int(columns[3])
        english = int(columns[4])
        history = int(columns[5])
        total_marks = math + science + english + history
        avg_marks = total_marks / 4.0
        print(f"{roll_no:<8} | {name:<10} | {math:<5} | {science:<7} | {english:<7} | {history:<7} | {total_marks:<5} | {avg_marks:<7.2f}")
        
        if (total_marks > highest_score):
            highest_score = total_marks
            top_student_name = name
        total_class_score += total_marks
        num_students += 1
overall_class_avg = total_class_score / num_students

print("\n--- Analytics ---")
print(f"Highest Scorer: {top_student_name} with {highest_score} total marks.")
print(f"Overall Class Average (Total Marks): {overall_class_avg:.2f}")
