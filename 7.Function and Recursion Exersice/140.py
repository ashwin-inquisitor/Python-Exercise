'''Find all armstrong numbers between two interval using function.'''

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n

def find_armstrong_upto(start, end):
    armstrong = []
    for num in range(start, end + 1):
        if is_armstrong(num):
            armstrong.append(num)
    return armstrong

try:
    start = int(input("Enter start of interval: "))
    end = int(input("Enter end of interval: "))

    if start > end:
        print("Invalid range. Start should be less than or equal to end.")
    else:
        result = find_armstrong_upto(start, end)
        print(f"\nArmstrong numbers between {start} and {end}:")
        print(result if result else "None found in this range.")

except ValueError:
    print("Invalid input! Please enter a integer.")