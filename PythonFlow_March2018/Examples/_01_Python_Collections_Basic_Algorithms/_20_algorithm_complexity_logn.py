"""O(log(n)) - Logarithmic
Binnary search as example"""

counter = 0
list_1 = list(range(0, 2**10))  # 1024
list_2 = list(range(0, 2**15))  # 32768


def binarySearch(list, item):
    global counter
    counter += 1

    if len(list) == 0:
        return False
    else:
        midpoint = len(list) // 2
        if list[midpoint] == item:
            return True
        else:
            if item < list[midpoint]:
                return binarySearch(list[:midpoint], item)
            else:
                return binarySearch(list[midpoint + 1:], item)


print(binarySearch(list_1, 0), counter)  # 11
counter = 0

print(binarySearch(list_2, 32768), counter)  # 16
counter = 0
