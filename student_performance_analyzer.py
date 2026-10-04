import numpy as np
marks = np.array([[78, 85, 92, 67],
                  [55, 72, 68, 80],
                  [90, 88, 95, 91],
                  [62, 58, 70, 65],
                  [84, 76, 89, 73]])

subjects = np.array(["Math", "physics", "Programming", "BEE"])
names = np.array(["Pranav", "Rahul", "Harshad", "Satvik", "Vedant"])
print("-"*5, "Total Marks", "-"*5)
total_marks = np.sum(marks, axis=1)

for i in range(len(total_marks)):
    print(f"{names[i]} -> {total_marks[i]}")

print()
print("-"*5, "Total Average of Marks", "-"*5)
average = np.mean(marks, axis=1)

for i in range(len(average)):
    print(f"{names[i]} -> {average[i]}")

print()
print("-"*5, "Topper", "-"*5)
topper = np.argmax(total_marks)
print(f"The topper of the class is {names[topper]} with {total_marks[topper]}")

print()
print("-"*5, "Highest Marks in each subject", "-"*5)
highest = np.max(marks, axis=0)

for i in range(len(highest)):
    print(f"{subjects[i]} -> {highest[i]}")

print()
print("-"*5, "Passed Students", "-"*5)
passed = np.all(marks >= 40, axis=1)
print(names[passed])

print()
print("-"*5, "Students Above 75 Average", "-"*5)
avg = average > 75
students = names[avg]
print(students)

print()
print("-"*5, "Grade Classification", "-"*5)
conditions = [average >= 85, average >= 75, average < 75]
choices = ["A", "B", "C"]
grades = np.select(conditions, choices, default="Fail")

for i in range(len(grades)):
    print(f"{names[i]} -> {grades[i]}")

print()
print("-"*5, "Subject-wise Average", "-"*5)
subject_average = np.mean(marks, axis=0)

for i in range(len(subject_average)):
    print(f"{subjects[i]} -> {subject_average[i]}")

print()
print("-"*5, "Student Who scored more than 80 in Programming", "-"*5)
subject_marks = marks[:, 2]
above_80 = subject_marks > 80
print(names[above_80])

print()
print("-"*5, "Number of Student passed all subjects", "-"*5)
passed_student = np.sum(passed)
print(f"NUmber of student passed : {passed_student}")
