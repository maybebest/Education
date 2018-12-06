"""Deque"""

from collections import deque

MY_QUEQUE = deque([], 5)

MY_QUEQUE.extendleft([1, 2, 3, 4, 5])
print(MY_QUEQUE)
# deque([5, 4, 3, 2, 1], maxlen=5)

MY_QUEQUE.appendleft(6)
print(MY_QUEQUE)
# deque([6, 5, 4, 3, 2], maxlen=5)

MY_QUEQUE.rotate(1)
print(MY_QUEQUE)
# deque([2, 6, 5, 4, 3], maxlen=5)

print(MY_QUEQUE.pop())  # 3
