'''Enter month number between(1-12) and print number of days in month using if else.'''

month = int(input("Enter month number (1-12) : "))
days_in_month = [31, 28, 31, 30, 31, 30,
                 31, 31, 30, 31, 30, 31]
if 1 <= month <=12:
    print("Month " +str(month) +" has " +str(days_in_month[month - 1]) +" days.")
else:
    print("Invaalid input! Enter the month between (1 - 12).")