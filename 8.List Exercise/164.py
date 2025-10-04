'''Insert an element in an array.'''

try:
    user_input = input("Enter elements separated by space: ")
    array = user_input.split()

    element = input("Enter element to insert: ")
    position = int(input("Enter the position (0-based index): "))

    if 0 <= position <= len(array):
        array.insert(position, element)
        print(f"Updated array: {array}")
    else:
        print(f"Invalid position! Must be between 0 and {len(array)}.")
except Exception as e:
    print(f"Something went wrong {e}!")