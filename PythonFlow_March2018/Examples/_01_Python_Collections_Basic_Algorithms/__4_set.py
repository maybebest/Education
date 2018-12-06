"""SET"""

PERSON_SET = {'Jack', 27, 'USA', 'New York', 27}
PERSON_SET = set(['Jack', 27, 'USA', 'New York', 27])

print(PERSON_SET)  # {'New York', 27, 'USA', 'Jack'}

PERSON_SET.add(42)
PERSON_SET.update('42')

print(PERSON_SET) # {'2', '4', 42, 'Jack', 'New York', 27, 'USA'}

PERSON_SET.discard('4')
# will raise an error if the item does not exist in the set
PERSON_SET.remove('2')

# remove and return random element
print(PERSON_SET.pop())
print(PERSON_SET)  # {'New York', 'Jack', 'USA', 27}

