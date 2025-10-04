'''Find reverse of an array.'''

user_input = input("Enter elements separated by space: ")
array = user_input.split()

reversed_array = array[::-1]

print(f"Original array is {array}.")
print(f"Reversed array is {reversed_array}.")