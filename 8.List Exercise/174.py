'''Sort array elements in ascending or descending order.'''
def sort_array(arr, order='asc'):
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

convert_array = []
for item in array:
    if item.isdigit() or (item.startswith('-') and item[1:].isdigit()):
        convert_array.append(int(item))
    elif item.count('.') == 1 and item.replace('.','',1).isdigit():
        convert_array.append(float(item))
    elif item.startswith('-') and item[1:].count('.') == 1 and item[1:].replace('.','',1).isdigigt():
        convert_array.append(float(item))
    else:
        convert_array.append(item)

sorted_array = sort_array(convert_array, order)
print(f"Sorted array: {sorted_array}.")