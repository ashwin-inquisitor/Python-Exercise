'''Find all prefect numbers between two interval using function.'''

def is_perfect(n):
    if n < 2:
        return False
    return sum(i for i in range(1, n) if n % i ==0 ) == n

def find_perfect_upto(start, end):
    perfect = []
    for num in range(start, end + 1):
        if is_perfect(num):
            perfect.append(num)
    return perfect

try:
    start = int(input("Enter start of interval: "))
    end = int(input("Enter end of interval: "))

    if start > end:
        print("Invalid range! Start should be less than or equal to range.")
    else:
        result = find_perfect_upto(start, end)
        print(f"Prefect numbers between {start} and {end}:")
        print(result if result else "None found in this range.")
except ValueError:
    print("Invalid input! Please Enter a integer. ")