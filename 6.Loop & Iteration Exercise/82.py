'''Count the frequency of digits in a given number.'''

num = int(input("Enter any number: "))
frequency = [0] * 10

while (num!=0):
    digit = num % 10
    frequency[digit] += 1
    num = num // 10

print("Digit frequency:")
for i in range(10):
    if frequency[i] > 0:
        print("Digit {}: {} time(s). ".format(i, frequency[i]))