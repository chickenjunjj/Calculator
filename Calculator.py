print("Type 1 to do an addition, 2 to do a subtraction, 3 to do a multiplication, 4 to do a division, 5 to get a percentage and 6 to get a letter grade.")
number = input()
if number == "1":
    input1 = input("Enter your first number:")
    input2 = input("Enter your second number:")
    print(float(input1) + float(input2))
if number == "2":
    input1 = input("Enter your first number:")
    input2 = input("Enter your second number:")
    print(float(input1) - float(input2))
if number == "3":
    input1 = input("Enter your first number:")
    input2 = input("Enter your second number:")
    print(float(input1) * float(input2))
if number == "4":
    input1 = input("Enter your first number:")
    input2 = input("Enter your second number:")
    print(float(input1) / float(input2))
if number == "5":
    input1 = input("Enter your first number:")
    input2 = input("Enter your second number:")
    print((float(input1) / float(input2)) * 100)
if number == "6":
    input1 = input("Enter your first number:")
    input2 = input("Enter your second number:")
    grade = ((float(input1) / float(input2)) * 100)
    if grade >= 90:
        print("A+")
    if grade >= 80 and grade < 90:
        print("A")
    if grade >= 70 and grade < 80:
        print("B+")
    if grade >= 60 and grade < 70:
        print("B")
    if grade >= 50 and grade < 60:
        print("C+")
    if grade >= 40 and grade < 50:
        print("C")
    if grade >= 30 and grade < 40:
        print("D+")
    if grade >= 20 and grade < 30:
        print("D")
    if grade < 20:
        print("F")
