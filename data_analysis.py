import pandas as pd

# Load CSV dataset
data = pd.read_csv("student_data.csv")

print("\n========== STUDENT DATASET ==========\n")
print(data)

# Check missing values
print("\n========== MISSING VALUES ==========\n")
print(data.isnull().sum())

# Average marks
average_marks = data["Marks"].mean()

print("\n========== CLASS ANALYSIS ==========\n")
print(f"Average Marks : {average_marks}")

# Highest marks
highest_marks = data["Marks"].max()
print(f"Highest Marks : {highest_marks}")

# Top performers
top_students = data[data["Marks"] > 85]

print("\n========== TOP PERFORMERS ==========\n")
print(top_students)

# Group by department
department_group = data.groupby("Department")["Marks"].mean()

print("\n========== DEPARTMENT ANALYSIS ==========\n")
print(department_group)

# Insights
print("\n========== INSIGHTS ==========\n")
print("1. Average class performance is good.")
print("2. Students scoring above 85 are top performers.")
print("3. CSE department students performed well.")
print("4. Data analysis completed successfully.")