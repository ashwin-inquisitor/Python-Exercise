'''Find sum of all array elements. – using recursion.'''
def recursive_sum(arr):
    if not arr:
        return 0
    return arr[0] + recursive_sum(arr[1:])

try:
    user_input = input("Enter number separeted by space: ")
    numbers = list(map(int, user_input.split()))

    total = recursive_sum(numbers)
    print(f"Sum of an array elements: {total}.")

except ValueError:
    print("Invalid input! Please enter an integer.")