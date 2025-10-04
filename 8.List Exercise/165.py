'''Delete an element from an array at specified position.'''

try:
    user_input = input("Enter element separated by space: ")
    array = user_input.split()

    position = int(input("Enter position to delete (0-based on index):"))

    if 0 <= position <= len(array):
        removed = array.pop(position)
        print(f"Deleted element is {removed}.")
        print(f"Updated array is {array}.")
    else:
        print(f"Invalid position! Must be between 0 and {len(array) - 1}.")
except Exception as e:
    print(f"Something went wrong {e}.")