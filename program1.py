def check_number(num):
    if num > 0:
        if num % 2 == 0:
            return f"{num} is a positive even number."
        else:
            return f"{num} is a positive odd number."
    elif num < 0:
        if num % 2 == 0:
            return f"{num} is a negative even number."
        else:
            return f"{num} is a negative odd number."
    else:
        return "The number is zero."
# Example usage
print(check_number(10))   # Output: 10 is a positive even number.
    