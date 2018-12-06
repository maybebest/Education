'''
- Implement your own _map function.
  first arg is collection, second arg - callback (mapper)
  function returns new collection of mapped items.
  Usage of standard map functionality is forbidden.
'''

lst = ['Jack', 27, 'USA', 5, "Jack", 'New York', 27, 44, 44]

def to_string(x):
    return str(x)

def _map(coll, func):
    out = []
    for m in coll:
        out.append(func(m))
    return out

print _map(lst, to_string)