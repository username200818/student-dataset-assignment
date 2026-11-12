import csv

# Fictional student dataset
students = [
    ["STU001", "Computer Science", 100, 95, 87],
    ["STU002", "Accounting", 200, 88, 76],
    ["STU003", "Mass Communication", 300, 92, 81],
    ["STU004", "Business Administration", 100, 79, 69],
    ["STU005", "Computer Science", 400, 96, 91],
    ["STU006", "Political Science", 200, 84, 73],
    ["STU007", "Economics", 300, 90, 78],
    ["STU008", "Accounting", 400, 75, 66],
    ["STU009", "Computer Science", 200, 89, 82],
    ["STU010", "Mass Communication", 100, 93, 85],
    ["STU011", "Business Administration", 300, 81, 71],
    ["STU012", "Economics", 400, 97, 89],
    ["STU013", "Political Science", 100, 86, 74],
    ["STU014", "Accounting", 300, 91, 80],
    ["STU015", "Computer Science", 300, 78, 68],
]

headers = [
    "Student ID",
    "Department",
    "Level",
    "Attendance Percentage",
    "Average Examination Score",
]

# Save the dataset as a CSV file
with open("students.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(students)

print("Student dataset created successfully!")
print(f"Total students: {len(students)}")
