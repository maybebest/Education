"""O(2^N) denotes an algorithm whose growth doubles with each addition
to the input data set. The growth curve of an O(2N) function is
exponential - starting off very shallow, then rising meteorically.
An example of an O(2^N) function is the recursive calculation of Fibonacci numbers
"""

i = 0
def fibonacci(number):
    global i
    i += 1
    if number <= 1:
        return number

    return fibonacci(number - 2) + fibonacci(number - 1)


print('fibonacci 16th number: %s; Function calls: %s' %
      (fibonacci(16), i))  # fibonacci 16th number: 987; Function calls: 3193

print('fibonacci 18th number: %s; Function calls: %s' %
      (fibonacci(18), i))  # fibonacci 18th number: 2584; Function calls: 11554

print('fibonacci 20th number: %s; Function calls: %s' %
      (fibonacci(20), i))  # fibonacci 20th number: 6765; Function calls: 33445

