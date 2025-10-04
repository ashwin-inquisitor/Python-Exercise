'''Delete all duplicate elements from an array.'''

user_input = input("Enter elements separated by space: ")
array = user_input.split()

unique_array = []
for item in array:
    if item not in unique_array:
        unique_array.append(item)

print(f"Array after deleting duplicate: {unique_array}.")