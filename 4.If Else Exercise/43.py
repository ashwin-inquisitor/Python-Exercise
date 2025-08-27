'''check leap year using if else.'''

year = int(input("Enter a year : "))

if ((year % 4 ==0 ) and (year % 100 !=0)) or (year % 400 == 0):
    print(str(year)+" is leap year.")
else:
    print(str(year)+" is not leap year.")