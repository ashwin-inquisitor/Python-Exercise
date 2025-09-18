'''Check whether a number is palindrome or not using recursion.'''

def rev_of_num(n, rev=0):
    if n == 0:
        return rev
    return rev_of_num(n // 10, rev * 10 + n % 10)

def is_palindrome(n):
    return n == rev_of_num(n)

try:
    num = int(input("Enter number to check is palindrome or not: "))
    if num < 0:
        print("Negative number is not consider a palindrome.")
    else:
        if is_palindrome(num):
            print(f"{num} is a palindrome.")
        else:
            print(f"{num} is not palindrome.")

except ValueError:
    print("Invalid input! Please enter an integer.")