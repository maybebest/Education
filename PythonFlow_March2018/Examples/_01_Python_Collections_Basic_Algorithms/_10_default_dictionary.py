"""defaultdict"""

from collections import defaultdict

USER = defaultdict(lambda: None)

USER['firstname'] = 'Vincent'
USER['lastname'] = 'Vega'

print(USER)
# defaultdict(<function <lambda> at 0x7f84f0ba4400>,
# {'lastname': 'Vega', 'firstname': 'Vincent'})

print(USER['firstname'])  # Vincent
print(USER['address'])  # None
print({}['address'])  # KeyError: 'address'
