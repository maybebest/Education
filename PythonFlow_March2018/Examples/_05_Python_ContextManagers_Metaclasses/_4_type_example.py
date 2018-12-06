"""Type"""

A = 1
B = '2'

print(A.__class__)  # <class 'int'>
print(B.__class__)  # <class 'str'>

print(A.__class__.__class__)  # <class 'type'>
print(B.__class__.__class__)  # <class 'type'>
