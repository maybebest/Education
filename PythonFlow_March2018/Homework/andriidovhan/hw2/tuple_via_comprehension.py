TEST=iter(tuple(i for i in range(-3, 18, 2)))

print(next(TEST))
print(next(TEST))

for i in TEST:
    print(i)