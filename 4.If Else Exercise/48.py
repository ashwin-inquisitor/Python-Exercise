''' input week number(1-7) and print the 
corresponding day of week name using if else.'''

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

week_num = int(input("Enter a week number(1-7) : "))

if 1 <= week_num <= 7:
    print(weekdays[week_num - 1])
else:
    print("Invalid input! Please enter number between 1 and 7.")