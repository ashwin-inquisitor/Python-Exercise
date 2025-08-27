'''Enter principle(p), rate of interest(r), and time period(t) and find compound interest.'''

p = float(input("Enter the principle amount : "))
r = float(input("Enter the rate of inetrest : "))
t = float(input("Enter the time period : "))

CI = p * (1 + r / 100) ** t

print("Compund interest for the amount is {:.2f}".format(CI))