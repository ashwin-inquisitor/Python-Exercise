'''Sort array elements in ascending or descending order.'''
def sort_array(arr, order = 'asc'):
    if order == 'asc':
        return sorted(arr)
    elif order == 'desc':
        return sorted(arr, reverse = True)
    else:
        print("Invalid sort array. use 'asc' or 'desc'. ")
    return arr
    

user_input = input("Enter elements separated by space: ")
array = user_input.split()

order = input("Enter sort order ('asc' for ascending, 'desc' for descending): ").lower()

converted_array = []
for item in array:
    try:
        if '.' in item:
            converted_array.append(float(item))
        else:
            converted_array.append(int(item))
    except ValueError:
        converted_array.append(item)

if all(isinstance(x, (int, float)) for x in converted_array):
    sorted_array = sort_array(converted_array, order)
elif all(isinstance(x, str) for x in converted_array):
    sorted_array = sort_array(converted_array, order)
else:
    print("Mixed types detected. Sorting as strings.")
    sorted_array = sort_array([str(x) for x in converted_array], order)


print(f"Sorted array: {sorted_array}.")