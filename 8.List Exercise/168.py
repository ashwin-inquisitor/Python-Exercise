'''Count total number of duplicate elements in an array.'''

user_input = input("Enter elements separated by space: ")
array = user_input.split()

frequency = {}
for item in array:
    frequency[item] = frequency.get(item, 0) + 1

duplicate_count = sum(1 for count in frequency.values() if count > 1)

print(f"Total duplicate elements in the array is {duplicate_count}.")