'''Input a number from user and find all the factors of the given number using for loop.'''

num = int(input("Enter any number: "))

print("All the factors of {} are: ")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)
