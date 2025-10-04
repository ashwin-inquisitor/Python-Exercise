'''Count total number of negative elements in an array.'''
def count_negatives(arr):
    negative_count = 0
    for num in arr:
        if num < 0:
            negative_count += 1
    return negative_count

try:
    user_input = input("Enter elements separated by space: ")
    numbers = list(map(int, user_input.split()))

    negative = count_negatives(numbers)
    print(f"Total negative elements in array is {negative}.")
except ValueError:
    print("Invalid input! Please enter integers only.")