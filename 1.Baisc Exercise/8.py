'''convert given days days into years, weeks and days'''

days = int(input("Enter the days:"))

years = days / 365
weeks = (days - (years * 365)) / 7
days = days - (years * 365) + (weeks * 7)

print("Years :", years)
print("Weeks :", weeks)
print("Days : ", days)