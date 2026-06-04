# Buggy calculator - intentional bugs for testing

def divide(a, b):
    return a / b  # Bug: no division by zero check

def get_average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)  # Bug: crashes on empty list

def find_max(numbers):
    max_val = 0  # Bug: wrong initial value, fails for negative numbers
    for n in numbers:
        if n > max_val:
            max_val = n
    return max_val

def celsius_to_fahrenheit(c):
    return c * 9/5  # Bug: missing + 32
