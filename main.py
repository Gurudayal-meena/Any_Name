"""
Simple calculator program with functions and loops.
"""

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


def main():
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
