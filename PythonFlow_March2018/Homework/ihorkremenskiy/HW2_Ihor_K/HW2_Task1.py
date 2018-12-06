'''
- Implement generator function which returns filtered items of the given list (lazy _filter, items by request)
  print values using: next, loop
'''

'''SZ you generator expression is cool,
  but you need to implement a function wich retrives 2 arguemns (callback and items collection)
  and returns generator object. Generator object returns only that items for wich callback function returns True.
  Please adaptate your generator expression for this purpose.
'''
"""IK: Thanks for you comment SZ!
Actually, I am not sure that I got the task correctly. 
So, based on the lecture we had regarding the generators I assume that I have to use some function for filter (callback), 
some collection and my filter function that retrieves this callback and collection and based on set cycle and using yield 
returns requred results. So please let me know if I am thinking in a wrong way.
Will comment first solution
"""

'''
#First solution

my_odd_filter = (x for x in range(51) if x % 2 == 0)

print("Here is a list of 3 first odd items in range of the list 0-50:")

print(next(my_odd_filter))  # prints 1st item
print(next(my_odd_filter))  # prints 2nd item
print(next(my_odd_filter))  # prints 3rd item

print("Here is a list of all other items:")

for item in my_odd_filter:
    print(item)
'''

#Second solution:

def odd_filter(x):
    return x % 2 == 0


def my_filter(my_function, my_collection):
    for n in my_collection:
        if my_function(n):
            yield n


collection = range(0, 51)
result = my_filter(odd_filter, collection)

print("Here is a list of 3 first odd items in range of the list 0-50:")
print(next(result))  # prints 1st item
print(next(result))  # prints 2nd item
print(next(result))  # prints 3rd item


print("Here is a list of all items in range of the list 0-50:")
for item in my_filter(odd_filter, collection):
    print(item)