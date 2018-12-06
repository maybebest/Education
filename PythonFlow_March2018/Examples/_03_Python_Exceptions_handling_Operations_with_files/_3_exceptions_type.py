"""Exception Handling"""


def devide(a, b):
    try:
        print(a / b)
    except TypeError:
        print("Type Error")
        print((a, b))
    except ZeroDivisionError:
        print("Zero Division Error")
        print(a)
    else:
        print("Else Statement")


devide(10, 2)  # 5.0 # Else Statement

devide(10, 0)  # Zero Division Error 10

devide(10, '0')  # Type Error (10, '0')
