'''Enter the marks of five subject and calculate the total, average and percentage marks'''

English = float(input("Enter the marks for English: "))
Mathematics = float(input("Enter the marks for Mathematics: "))
Physics = float(input("Enter the marks for Physics: "))
Biology = float(input("Enter the marks for Biology: "))
Chemistry = float(input("Enter the marks for Chemistry: "))

total = English + Mathematics + Physics + Biology + Chemistry
average = total / 5
percentage = (total / 500) * 100

print("Total marks for 5 subject is {:.2f}".format(total))
print("Average marks for 5 subject is {:.2f}".format(average))
print("Percentage for 5 subject is {:.2f}".format(percentage))