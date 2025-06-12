try:
    n=int(input("Enter the number : "))
    s=12/n
    print(s)
except ZeroDivisionError:
    print("The number can't be divided by 0")
except ValueError:
    print("Input only the integer value.")
except Exception:
    print("Something went wrong!")
finally:
    print("The calculation is done.")

def calculator():
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            result = num1 / num2
        else:
            print("Invalid operator.")
            return
        
        print("Result:", result)

    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except ValueError:
        print("Please enter valid numbers only.")
    finally:
        print("Calculation complete.")

calculator()
