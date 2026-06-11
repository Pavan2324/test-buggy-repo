# Buggy calculator - intentional bugs for testing

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")  # Fix: Check for division by zero
    return a / b

def get_average(numbers):
    if not numbers:
        raise ValueError("Cannot compute average of an empty list")  # Fix: Check for empty list
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)

def find_max(numbers):
    if not numbers:
        raise ValueError("Cannot find max of an empty list")  # Fix: Check for empty list
    max_val = numbers[0]  # Fix: Initialize max_val to the first element of the list
    for n in numbers:
        if n > max_val:
            max_val = n
    return max_val

def celsius_to_fahrenheit(c):
    return c * 9/5 + 32  # Fix: Add 32 to the conversion formula

def get_first_element(lst):
    if not lst:
        raise ValueError("List is empty")  # Fix: Check for empty list
    return lst[0]

def string_to_int(s):
    try:
        return int(s)
    except ValueError:
        raise ValueError("Invalid input: cannot convert to integer")  # Fix: Add error handling for invalid input

def calculate_percentage(part, total):
    if total == 0:
        raise ValueError("Total cannot be zero")  # Fix: Check for total being zero
    return (part / total) * 100