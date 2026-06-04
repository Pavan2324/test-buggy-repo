# Buggy calculator - intentional bugs for testing

def divide(a, b):
    # Fix: Check for division by zero and raise an exception if b is zero
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def get_average(numbers):
    # Fix: Check if the list is empty and raise an exception if it is
    if not numbers:
        raise ValueError("Cannot compute average of an empty list")
    total = sum(numbers)  # Use sum() for simplicity and clarity
    return total / len(numbers)

def find_max(numbers):
    # Fix: Check if the list is empty and raise an exception if it is
    if not numbers:
        raise ValueError("Cannot find maximum of an empty list")
    max_val = numbers[0]  # Initialize max_val to the first element to handle negative numbers
    for n in numbers:
        if n > max_val:
            max_val = n
    return max_val

def celsius_to_fahrenheit(c):
    # Fix: Add 32 to the conversion formula to correctly convert Celsius to Fahrenheit
    return c * 9/5 + 32