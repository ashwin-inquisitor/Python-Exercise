'''Find sum of all even or odd numbers in given range using recursion.'''
def sum_of_even(start, end):
    if start > end:
        return 0
    return (start if start % 2 == 0 else 0) + sum_of_even(start + 1, end)
    
def sum_of_odd(start, end):
    if start > end:
        return 0
    return (start if start % 2 !=0 else 0) + sum_of_odd(start + 1, end)

try:
    start = int(input("Enter start of range: "))
    end = int(input("Enter end of range: "))
    choose = input("Enter your choice 'E' for even and 'O' for odd.\n").strip().upper()

    if choose == 'E':
        print(f"Sum of even number from {start} to {end} is {sum_of_even(start, end)}.")
    elif choose == 'O':
        print(f"Sum of odd number from {start} to {end} is {sum_of_odd(start, end)}.")
    else:
        print("Invalid input! Please enter 'E' for even and 'O' for odd.")

except ValueError:
    print("Invalid input! Please enter an integer.")