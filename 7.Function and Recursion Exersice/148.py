'''Find sum of digits of a given number using recursion.'''
def sum_of_digit(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digit(n // 10)

try:
    num = int(input("Enter number ot find sum of digits: "))
    result = sum_of_digit(abs(num))
    print(f"Sum of digits for {num} is {result}.")

except ValueError:
    print("Inavlid input! Please enter an integer.")