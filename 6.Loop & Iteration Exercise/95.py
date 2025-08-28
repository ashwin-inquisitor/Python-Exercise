'''WAP to print a fibonacci series upto nth terms.(using loop) '''

n = int(input("Enter the number of terms: "))

a = 0
b = 1

print("Fibonacci series :")
for i in range(n):
    print(a, end = " ")
    temp = a
    a = b
    b = temp + b