# sample_app.py

# Function
def greet(name):
    return f"Hello, {name}!"

# Class
class Calculator:
    def add(self, a, b):
        return a + b
    
    def multiply(self, a, b):
        return a * b

# Main program
def main():
    # User input
    name = input("Enter your name: ")
    print(greet(name))

    # Calculator usage
    calc = Calculator()
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Addition:", calc.add(a, b))
    print("Multiplication:", calc.multiply(a, b))

    # Loop example
    print("\nCounting from 1 to 5:")
    for i in range(1, 6):
        print(i)

    # List example
    fruits = ["apple", "banana", "orange"]
    print("\nFruits list:")
    for fruit in fruits:
        print(fruit)

    # File handling
    with open("output.txt", "w") as file:
        file.write(f"User: {name}\n")
        file.write(f"Addition: {calc.add(a, b)}\n")
        file.write(f"Multiplication: {calc.multiply(a, b)}\n")

    print("\nData saved to output.txt")

# Run program
if __name__ == "__main__":
    main()
