'''To check whether if the the number is even or odd using function.'''

def is_Even(number):
    return number % 2 == 0

number = int(input("Enter number to check even or odd: "))

if is_Even(number):
    print(f"{number} is Even.")
else:
    print(f"{number} is odd.")