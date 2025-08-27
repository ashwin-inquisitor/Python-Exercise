''' input a number and check positive negative or zero using switch case. '''

num = int(input("Enter a number: "))

match(num > 0, num < 0):
    case(True,False):
        print(num, "is positive.")
    case(False, True):
        print(num, "is negative.")
    case _:
        print(num, "is zero.")