

"""Counter"""

from collections import Counter

PHRASE = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do 
eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim 
veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo 
consequat."
"""

C1 = Counter(PHRASE).most_common(5)
print(C1)
# [(' ', 35), ('i', 23), ('e', 18), ('o', 18), ('t', 15)]

C1 = Counter(PHRASE.split(' ')).most_common(5)
print(C1)
# [('ut', 2), ('tempor', 1), ('ipsum', 1), ('consectetur', 1), ('exercitation', 1)]

