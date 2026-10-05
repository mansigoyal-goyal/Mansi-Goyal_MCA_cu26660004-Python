marks = int(input("Enter marks: "))

if marks >= 90 and marks <= 100:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: F")