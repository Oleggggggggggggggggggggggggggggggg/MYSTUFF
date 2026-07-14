def calculator():
    try:
        num1 = float(input("First"))
        num2 = float(input("Second"))
    except ValueError:
        print("NET NOMERA")
    finally:
        operator = input("Operator: ")
        if operator == "+":
            print(num1 + num2)
        elif operator == "-":
            print(num1 - num2)
        elif operator == "*":
            print(num1 * num2)
        elif  operator == "/":
            try:
                print(num1 / num2)
            except ZeroDivisionError:
                print("Can't divide by zero")
        else:
            print("Invalid operator")

calculator()
        
        

        
    