"""namedtuple(). CSV"""

from collections import namedtuple
import csv

CSV_STR = '''1997,Ford,E350,"ac, abs, moon",3000.00
1999,Chevy,"Venture ""Extended Edition""","",4900.00'''

CarRecord = namedtuple('CarRecord', 'Year, Make, Model, Description, Price')

cars = []
for str in csv.reader(CSV_STR.split('\n')):
    print(str)
    # ['1997', 'Ford', 'E350', 'ac, abs, moon', '3000.00']
    # ...
    cars.append(CarRecord._make(str))

print(cars)
# [
# CarRecord(Year='1997', Make='Ford', Model='E350', Description='ac, abs, moon', Price='3000.00'),
# CarRecord(Year='1999', Make='Chevy', Model='Venture "Extended Edition"', Description='', Price='4900.00')
# ]

print([cars[0].Make, cars[0].Model])
# ['Ford', 'E350']
