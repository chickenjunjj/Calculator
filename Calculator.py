class Calculator():
    def __init__(self):
        self.start()
        
    def start(self):
        print("[c] calculate")
        print("[q] quit")
        command = input()
        print("")
        if command == 'c':
            self.calculate()
        elif command == 'q':
            pass
        else:
            print("Invalid command")
            self.start()

    def calculate(self):
        print("[1] addition")
        print("[2] subtraction")
        print("[3] multiplication")
        print("[4] division")
        print("[5] percentage")
        print("[6] letter grade")
        number = input()
        print("")
        input1 = input("Enter your first number: ")
        input2 = input("Enter your second number: ")
        print("")
        self.switch_case(number, input1, input2)
        print("")
        self.start()
        
    def switch_case(self, number, input1, input2):
        switcher = {
            1: self.add,
            2: self.subtract,
            3: self.multiply,
            4: self.divide,
            5: self.percent,
            6: self.grade
        }
        switcher[int(number)](input1, input2)
        

    def add(self, input1, input2):    
        print(float(input1) + float(input2))
            
    def subtract(self ,input1, input2):
        print(float(input1) - float(input2))
            
    def multiply(self, input1, input2):
        print(float(input1) * float(input2))
            
    def divide(self, input1, input2):
        print(float(input1) / float(input2))
            
    def percent(self, input1, input2):
        print((str(float(input1) / float(input2) * 100) + "%"))
        
    def grade(self, input1, input2):
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
