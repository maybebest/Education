comp = tuple(x**3 for x in range(10))
print(comp, type(comp))
itr = iter(comp)
print(itr)

for i in range(len(comp)):
    print(i+1, 'next =>', next(itr))
