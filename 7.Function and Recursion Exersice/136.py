'''Input two or more numbers from user and find maximum and minimum of the given numbers using functions.'''

def find_max(numbers):
    return max(numbers)

def find_min(numbers):
    return min(numbers)

user_input = input("Enter two or more numbers separated by spaces: ")
numbers = list(map(float, user_input.split()))

if len(numbers) < 2:
    print("Please enter atleast two numbers.")
else:
    maximum = find_max(numbers)
    minimum = find_min(numbers)

print(f"Maximum number is {maximum}.")
print(f"Minimum number is {minimum}.")