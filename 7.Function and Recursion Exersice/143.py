'''Print all even or odd numbers in given range using recursion.'''

def print_even(start, end):
    if start > end:
        return
    if start % 2 == 0:
        print(start)
    print_even(start + 1, end)

def print_odd(start, end):
    if start > end:
        return
    if start % 2 != 0:
        print(start)
    print_odd(start + 1, end)

try:
    start = int(input("Enter start of range: "))
    end = int(input("Enter end of range: "))
    choose = input("Enter your choice to print even or odd? (E/O)\n").strip().upper()

    print(f"{choose} number between {start} and {end}:")
    if choose == 'E':
        print_even(start, end)
    elif choose == 'O':
        print_odd(start, end)
    else:
        print("Invalid input! Please Enter E for even and O for odd.")

except ValueError:
    print("Invalid input! Please enter an integer.")