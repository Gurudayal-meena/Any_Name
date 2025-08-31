"""
Simple calculator program with functions and loops.
"""

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b (a - b)."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return the division of a by b. If b is 0, return error message."""
    if b == 0:
        return "Error: Division by zero"
    return a / b

def main():
    """Run the simple calculator with predefined numbers."""
    print("Welcome to Simple Calculator")
    numbers = [(10, 5), (20, 0), (7, 3)]

    for a, b in numbers:
        print(f"\nNumbers: {a}, {b}")
        print(add(a, b))
        print(subtract(a, b))
        print(multiply(a, b))
        print(divide(a, b))

if __name__ == "__main__":
    main()
