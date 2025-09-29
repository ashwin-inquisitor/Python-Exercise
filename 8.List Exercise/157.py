'''Print all negative elements in an list.'''
def print_negative(lst):
    print("Negative numbers in list: ")
    for num in lst:
        if num < 0:
            print(num)
try:
    element = input("Enter list elements separated by space: ").split()
    numbers = [int(x) for x in element]
    print_negative(numbers)
except ValueError:
    print(f"Invalid input! Please enter integers only.")