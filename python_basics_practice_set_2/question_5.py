num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

operation = input("Enter operation (+, -, *, /): ")
match operation:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        if num2 != 0:
            print(num1 / num2)
    case _:
        print("Invalid operation! Please enter a valid operation (+, -, *, /).")