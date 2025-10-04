'''Count total number of even and odd elements in an array.'''
def count_even_odd(arr):
    even_count = odd_count = 0
    for num in arr:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count
try:
    user_input = input("Enter elements separated by space: ")
    numbers = list(map(int, user_input.split()))

    even, odd = count_even_odd(numbers)
    print(f"Total even number is {even}.")
    print(f"Total odd number is {odd}.")
except ValueError:
    print("Invalid input! Please enter an integer.")