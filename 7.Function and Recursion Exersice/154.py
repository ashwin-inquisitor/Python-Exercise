'''Find sum of elements of array using recursion.'''
def sum_of_list(lst, index = 0):
    if index >= len(lst):
        return 0
    return lst[index] + sum_of_list(lst, index + 1)
try:
    elements = input("Enter list of elements:").split()
    numbers = [int(x) for x in elements]
    result = sum_of_list(numbers)
    print(f"Sum of elements in list is {result}.")

except ValueError:
    print("Invalid input! please enter integer only.")