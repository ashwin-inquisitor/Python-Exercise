'''Merge two array to third array.'''

user_input = input("Enter elements of first array separated by space: ")
array1 = user_input.split()

user_input = input("Enter elements of second array separated by space: ")
array2 = user_input.split()

array3 = array1 + array2

print(f"First array :{array1}.")
print(f"Second array : {array2}.")
print(f"Merged array : {array3}.")