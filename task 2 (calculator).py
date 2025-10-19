def calculator():
    print("Simple Calculator")
    print("Operations: +  -  *  /")

    try:
        # Take user inputs
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose an operation (+, -, *, /): ")

        # Perform calculation
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero is not allowed.")
                return
        else:
            print("Invalid operation! Please choose +, -, * or /.")
            return

        # Display result
        print(f"Result: {num1} {operation} {num2} = {result}")

    except ValueError:
        print("Invalid input! Please enter numbers only.")

# Run the calculator
calculator()
