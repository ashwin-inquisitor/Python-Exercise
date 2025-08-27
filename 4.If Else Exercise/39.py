'''find maximum between three numbers using ladder if else or nested if. '''

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
num3 = int(input("Enter the third number : "))

if num1 > num2 and num1 > num3:
    max = num1
elif num2 > num3:
    max = num2
else:
    max = num3
print(str(max)+" is the maximum.")
