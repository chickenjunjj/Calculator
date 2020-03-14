class Calculator():
    def __init__(self):
        print("[1] addition")
        print("[2] subtraction")
        print("[3] multiplication")
        print("[4] division")
        print("[5] percentage")
        print("[6] letter grade")
        number = input()
        self.switch_case(number)
        
    def switch_case(self, number):
        switcher = {
            1: self.add,
            2: self.subtract,
            3: self.multiply,
            4: self.divide,
            5: self.percent,
            6: self.grade
        }
        switcher[int(number)]()    
        

    def add(self):    
        input1 = input("Enter your first number:")
        input2 = input("Enter your second number:")
        print(float(input1) + float(input2))
            
    def subtract(self):
        input1 = input("Enter your first number:")
        input2 = input("Enter your second number:")
        print(float(input1) - float(input2))
            
    def multiply(self):
        input1 = input("Enter your first number:")
        input2 = input("Enter your second number:")
        print(float(input1) * float(input2))
            
    def divide(self):
        input1 = input("Enter your first number:")
        input2 = input("Enter your second number:")
        print(float(input1) / float(input2))
            
    def percent(self):
        input1 = input("Enter your first number:")
        input2 = input("Enter your second number:")
        print((float(input1) / float(input2)) * 100)
        
    def grade(self):
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

calculator = Calculator()
