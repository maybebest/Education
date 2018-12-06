"""Doctest"""

def fibonacci(number):
    """Calculate Fibonacci number by index
    >>> fibonacci(25)
    75025
    >>> fibonacci(26)
    Fibonacci number should be less then 100500
    """
    if number <= 1:
        return number
    return fibonacci(number - 2) + fibonacci(number - 1)

if __name__ == "__main__":
    import doctest
    doctest.testmod()


