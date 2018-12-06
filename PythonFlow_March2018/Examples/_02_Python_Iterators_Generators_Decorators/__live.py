
from collections import deque

numbers = [1,2,3,4,5]

numbers_iter = iter(numbers)
numbers_iter2 = iter(numbers)

print(next(numbers_iter))
numbers[0] = 0
print(next(numbers_iter2))

