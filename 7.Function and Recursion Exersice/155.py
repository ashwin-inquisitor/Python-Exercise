'''Find maximum and minimum elements in array using recursion.'''
def find_max(lst, index = 0, current_max = None):
    if index >= len(lst):
        return current_max
    if current_max is None or lst[index] > current_max:
        current_max = lst[index]
    return find_max(lst, index + 1, current_max)

def find_min(lst, index = 0, current_min = None):
    if index >= len(lst):
        return current_min
    if current_min is None or lst[index] < current_min:
        current_min = lst[index]
    return find_min(lst, index + 1, current_min)

try:
    elements = input("Enter elements in list: ").split()
    numbers = [int(x) for x in elements]

    max_val = find_max(numbers)
    min_val = find_min(numbers)

    print(f"Maximum number in list is {max_val}.")
    print(f"Minimum number in list is {min_val}.")

except ValueError:
    print("Invalid input! Please enter integers only.")