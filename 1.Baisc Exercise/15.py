'''Enter principle, rate, and time (P, R, T) and find the simple interest rate.'''

P = float(input("Enter the principle amount : "))
R = float(input("Enter the rate of interest : "))
T = float(input("Enter the time period : "))

SI = (P * R * T) / 100

print("Simple interest for the amount is {:.2f}".format(SI))