'''Print all unique elements in the array.'''

user_input = input("Enter elements separated by space: ")
array = user_input.split()

unique_element = list(set(array))
print("Unique item in the array: ")
for item in unique_element:
    print(item)