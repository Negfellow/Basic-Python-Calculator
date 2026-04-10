# Basic Calculator

#Ask the user for the first number
num1 = float(input("Enter the first number:"))

#Ask the user for the second number
num2 = float (input("Enter the second number:"))

# Ask the user which operation they want to use
operation = input ("Enter an operation (+, -, *, /):")

# Use if statements to decide what to do
if operation =="+":
    result = num1 + num2
    print("The answer is:", result)

elif operation =="-":
    result = num1 - num2
    print("The answer is:", result)

elif operation == "*":
    result = num1 * num2 
    print("The answer is:", result)

elif operation == "/":
    if num2 !=0:
        result = num1 / num2
        print("The answer is:", result)
    else:
        print ("Error: You cannot divide by zero.")
else:
    print("Invalid operation. Please use +, -, *, or /.")
