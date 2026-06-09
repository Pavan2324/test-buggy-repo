# Buggy calculator - intentional bugs for testing

def divide(a, b):
    # Fix: Check for division by zero
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def get_average(numbers):
    # Fix: Check for empty list
    if not numbers:
        raise ValueError("Cannot compute average of an empty list")
    total = sum(numbers)  # Simplified summation using built-in sum function
    return total / len(numbers)

def find_max(numbers):
    # Fix: Check for empty list and initialize max_val to the first element
    if not numbers:
        raise ValueError("Cannot find max of an empty list")
    max_val = numbers[0]
    for n in numbers:
        if n > max_val:
            max_val = n
    return max_val

def celsius_to_fahrenheit(c):
    # Fix: Add 32 to the conversion formula
    return c * 9/5 + 32

def get_first_element(lst):
    # Fix: Check for empty list
    if not lst:
        raise ValueError("List is empty")
    return lst[0]

def string_to_int(s):
    # Fix: Add error handling for invalid integer conversion
    try:
        return int(s)
    except ValueError:
        raise ValueError("Invalid integer string")

def calculate_percentage(part, total):
    # Fix: Check for total = 0
    if total == 0:
        raise ValueError("Total cannot be zero")
    return (part / total) * 100