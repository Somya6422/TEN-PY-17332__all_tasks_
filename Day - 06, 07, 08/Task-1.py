'''BUG 1 — RUNTIME ERROR
    Type  : ZeroDivisionError
    Cause : Attempting to calculate the average by dividing the total sum by 0 instead of the number of students.
    Fix   : Replace the hardcoded 0 with the actual length of the marks list (len(marks)).

        BUGGY CODE:
            marks = [85, 90, 92, 78, 88]
            total = sum(marks)
            average = total / 0  # Crashes the program

        FIXED CODE:
            marks = [85, 90, 92, 78, 88]
            total = sum(marks)
            average = total / len(marks)


BUG 2 — LOGICAL ERROR
    Type  : Logical Error
    Cause : Using the max() function when attempting to find the lowest mark, resulting in the highest mark being returned instead.
    Fix   : Replace max(marks) with min(marks) to correctly identify the lowest score.

        BUGGY CODE:
            marks = [85, 90, 92, 78, 88]
            lowest = max(marks)  # Logically incorrect

        FIXED CODE:
            marks = [85, 90, 92, 78, 88]
            lowest = min(marks)
'''

# FINAL WORKING PROGRAM

def main():
    marks = []
    print("--- Student Marks Calculator ---")
    print("Please enter the marks for 5 students.")
    for i in range(5):
        while True:
            try:
                mark = float(input(f"Enter marks for Student {i + 1}: "))
                if mark < 0 or mark > 100:
                    print("Please enter a valid mark between 0 and 100.")
                    continue
                marks.append(mark)
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
    total_marks = sum(marks)
    average_marks = total_marks / len(marks)
    highest_mark = max(marks)
    lowest_mark = min(marks)
    print("\n--- Final Results ---")
    print(f"Total Marks   : {total_marks}")
    print(f"Average Marks : {average_marks:.2f}")
    print(f"Highest Marks : {highest_mark}")
    print(f"Lowest Marks  : {lowest_mark}")

if __name__ == "__main__":
    main()
