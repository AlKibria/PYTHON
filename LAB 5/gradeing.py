marks = int(input("Enter the student's marks: "))

if marks >= 90:
    print("Grade: A+")
elif marks >= 85 and marks <= 89:
    print("Grade: A")
elif marks >= 80 and marks <= 84:
    print("Grade: B+")
elif marks >= 60 and marks <= 79:
    print("Grade: Pass")
elif marks>100:
    print("Invalid marks entered.")
else:
    print("Grade: Fail")