'''Find second largest element in an array.'''
def second_largest(arr):
    if len(arr) < 2:
        return None
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second

try:
    user_input = input("Enter numbers separated by spaces: ")
    numbers = list(map(int, user_input.split()))

    result = second_largest(numbers)
    if result is not None:
        print(f"Second largest element in an array is {result}.")
    else:
        print("Array must contain atleast to distinct two elements.")
except ValueError:
    print("Invalid input! Please enter an integer.")