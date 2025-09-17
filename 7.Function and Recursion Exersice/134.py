'''Find cube of any number using function.'''

def find_cube(num):
    return  num ** 3
     
number = int(input("Enter number to find cube: "))
result = find_cube(number)

print(f"Cube of the {number} is {result}.")