'''Enter two numbers and find maximum
 between two numbers using conditional/ternary operator'''

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

num_max = a if a > b else b

print("The maximum number is " +str(num_max))