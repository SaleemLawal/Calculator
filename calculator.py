
def calculator(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == '-':
        return num1 + num2
    elif operator == '/':
        return num1 / num2
    elif operator == '*':
        return num1 * num2



def main():
    num1 = int(input("Enter first number: "))
    operator = input('Enter the operator: ')
    num2 = int(input('enter second number: '))
    result = calculator(num1, operator, num2)
    print(result)
    
main()
    
    
# Define a function that takes in two numbers and an operator, and returns the result of the operation applied to the numbers.
# Define a main function that prompts the user for input, obtains the user's input, and calls the function from step 1 with the appropriate arguments.
# Call the main function to start the calculator.