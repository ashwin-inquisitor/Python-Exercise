'''Search an element in an array.'''

user_input = input("Enter elements separated by sapce: ")
array = user_input.split()

target = input("Enter the element to search: ")
if target in array:
    print(f"Element '{target}' found at index {array.index(target)}.")
else:
    print(f"Element '{target}' not found in array.")