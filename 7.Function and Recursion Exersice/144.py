'''Find sum of all natural numbers between 1 to n using recursion.'''

def sum_range(start, end):
    if start > end:
        return 0
    return start + sum_range(start + 1, end)

try:
    start = int(input("Enter start of range: "))
    end = int(input("Enter end of range: "))

    if start < 1 and end < 1:
        print("Please! Enter natural number(>= 1).")
    elif start > end:
        print("Start should be less than or equal to end.")
    else:
        result = sum_range(start, end)
        print(f"Sum of number between {start} and {end} is {result}.")

except ValueError:
    print("Invalid input! Please enter a integer.")