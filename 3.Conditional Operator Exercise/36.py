'''Enter a year and check whether year 
is leap year or not using conditional/ternary operator '''

year = int(input("Enter a year to check it's a leap year: "))

leap_year = "leap" if ( year%400 == 0 or (year % 4 == 0 and year % 100 !=0)) else "not leap"

print("The year is " +str(leap_year)+ " year.")