collection = list(x**2+5 for x in range(1, 11))

print(collection)

'''AM
Please use generetor expression here:

def my_find(col, callback_func): #collection could be just a list or tuple, not exact iterator
    return next((<<your generator expression here>>), None)
'''

'''AM 2 (not for rework)
1) 
Your functions should be reusable and generic
It's great if you are able to use it in different case
Additional string in return statement could complicate usage of your function.
So please just return a value from your function and move additional print info outside of you function
2) 
next(gen) could cause an error if nothing found
so some default value could be passed as second param:
next(gen, 'No matches found!')
'''
def my_find(col, callback_func):
    gen = (i for i in col if callback_func(i))
    return 'First matched to filter item from collection: {0}'.format(next(gen))


def is_simple_check(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    print(n, 'is simple number')
    return True


print(my_find(collection, is_simple_check))
