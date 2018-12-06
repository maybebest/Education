'''
- Implement your own _find function using generator expression.
  first arg is callback, second arg - collection.
  function returns first item from collection for which callback function call return true
  generator expression usage required.
'''

'''SZ you need to implement a function wich retrives 2 arguments (callback and collection)
  and using generator return first value for wich callback function returns True
  
  IK: So, what I got from the comment above - the realisation of this task is same with HW2 Task 1 (of course, if 1st task is completed as expected :) )
  Like I did in Task 1, I can define any filter function and then call it in  my generator expression and retreive collection
  as an argument. That will be same with 1st task
  What if for this task I set the filter inside the generator expression? The solution is below 
'''

''''#first implemented solution is commented
my_list = range(2, 20)
GEN_EXP_FIND = (x for x in my_list if x % 2 != 0)
print("First odd number from the list is:")
print(next(GEN_EXP_FIND))
 In additional to load others items
print ("Second odd number from the list is:")
print(next(GEN_EXP_FIND))
print ("Third odd number from the list is:")
print(next(GEN_EXP_FIND))
'''

'''AM 2
"- Implement your own _find function using generator expression."
Here i meant following construction:
def _find(condition_cb, collection):
  GEN_EXP_FIND = (x for x in my_list if x % 2 != 0) # you should use collection and condition_cb here in if statement 
  return next(GEN_EXP_FIND, 'No matches found!')  

print(_find(lambda n: n % 2 == 0, [1,3,4,5]))
#4
'''

# Second implemented solution:

def my_gen_exp(my_function, my_collection):
    for item in my_collection:
        if item % 2 != 0:
            yield item


collection = range(0, 21)

GEN_EXP = my_gen_exp(my_gen_exp, collection)

print((next(GEN_EXP)))
print((next(GEN_EXP)))
print((next(GEN_EXP)))