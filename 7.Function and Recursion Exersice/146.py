'''find reverse of any number using recursion.'''
def rev_of_num(n, rev=0):
    if n == 0:
        return rev
    return rev_of_num(n // 10, rev * 10 + n % 10)

try:
    num = int(input("Enter number to find its reverse: "))
    reversed_num = rev_of_num(abs(num))
    if num < 0:
        reversed_num = -reversed_num
    print(f"Reversed number of {num} is {reversed_num}.")

except ValueError:
    print("Invalid input! Please enter an integer.")