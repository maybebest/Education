def fibonacci(number):
    """Calculate Fibonacci number by index"""
    if number <= 1:
        return number
    return fibonacci(number - 2) + fibonacci(number - 1)
