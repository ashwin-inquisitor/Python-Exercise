'''input basic salary of an employee and 
calculate gross salary according to given conditions.
Basic Salary <= 10000 : HRA = 20%, DA = 80%
Basic Salary is between 10001 to 20000 : HRA = 25%, DA = 90%
Basic Salary >= 20001 : HRA = 30%, DA = 95%'''

bs = int(input("Enter basic salary of an employee: "))

if bs <= 10000:
    hra = bs * 0.2
    da = bs * 0.8
elif bs <= 20000:
    hra = bs * 0.25
    da = bs * 0.9
elif bs >= 20001:
    hra = bs * 0.3
    da = bs * 0.95

gross_salary = bs + hra + da

print("Basic salary: {:.2f}".format(bs))
print("HRA: {:.2f}".format(hra))
print("DA: {:.2f}".format(da))
print("Gross salary: {:.2f}".format(gross_salary))