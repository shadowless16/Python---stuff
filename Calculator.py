trigger = input("Do you want to perform a calculation?(Y)")
while trigger == "Y" :
 operator = input("Select (+, /, -, *)")
 Num1 = float(input("first number"))
 print("Number Accepted")
 Num2 = float(input("second number"))
 print("Number Accepted")

 if operator == "+":
     Result = Num1 + Num2
     print(Result)
     trigger == input("Do you wish to perform another calculation?(Y)")
 elif operator == "/":
     Result = Num1 / Num2
     print(Result)
     trigger == input("Do you wish to perform another calculation?(Y)")
 elif operator == "-":
     Result = Num1 - Num2
     print(Result)
     trigger == input("Do you wish to perform another calculation?(Y)")
 elif operator == "*":
     Result = Num1 * Num2
     print(Result)
     trigger == input("Do you wish to perform another calculation?(Y)")
 else:
     print("This is not an operator, dumbass")
else:
    print(f"No calculation shall be carried out then")