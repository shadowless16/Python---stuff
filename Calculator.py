trigger = input("Do you want to perform a calculation?(Y)").upper().strip()
while trigger == "Y" :
    try:
        Num1 = float(input("first number: "))
        print("Number Accepted")
        Num2 = float(input("second number: "))
        print("Number Accepted")
        operator = input("Select (+, /, -, *): ")

        if operator == "+":
            Result = Num1 + Num2
            print(Result)
        elif operator == "/":
            Result = Num1 / Num2
            print(Result)
        elif operator == "-":
            Result = Num1 - Num2
            print(Result)
        elif operator == "*":
            Result = Num1 * Num2
            print(Result)
        else:
            print("This is not an operator, dumbass")
            print(f"No calculation shall be carried out then")

        trigger = input("Do you want to another perform a calculation?(Y)").upper().strip()
    except ValueError:
        print("Invlaid")


#corrections made
#for the trigger variable you werent case sensetive
#the operator vaildator was supposed to be carried out on the spot the moment the operator is inputted not when the operation is taking place
#you didn't handle the error for when a user enters a letter in the varibale for the numbers
#you were supposed to call the operator varible after the numbers varible 
#you were calling the trigger multiple times in the if blocks which causes the code to be redundant 