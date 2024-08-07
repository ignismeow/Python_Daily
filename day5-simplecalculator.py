# Problem: Making a simple calculator
def sum(num1, num2):
    result =  num1 + num2
    print(f"Adding {num1} with {num2} gives {result}")
    
def subtraction(num1, num2):
    result =  num1 - num2
    print(f"Substracting {num1} with {num2} gives {result}")
    
def multiplication(num1, num2):
    result =  num1 * num2
    print(f"Multiplying {num1} with {num2} gives {result}")
    
def division(num1, num2):
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result =  num1 / num2
        print(f"Dividing {num1} with {num2} gives {result}")

def main():
    while True:
        print("\nSimple Calculator")
        print("1. Add")
        print("2. Subract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("Enter your choice(1-5): ")
        
        if choice == '5':
            print("Exiting the calculator Goodbye!")
            quit()
            
        num1 = float(input('Please enter first number: '))
        num2 = float(input('Please enter Second number: '))
        
        if choice == "1":
            sum(num1, num2)
        elif choice == "2":
            subtraction(num1, num2)
        elif choice == "3":
            multiplication(num1, num2)
        elif choice == "4":
            division(num1, num2)
        else:
            print("Invalid number please enter a valid number.")
            
if __name__ == "__main__":
    main()
