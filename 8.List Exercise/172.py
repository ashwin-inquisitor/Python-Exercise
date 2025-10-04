'''Put even and odd elements of array in two separate array.'''
def separate_even_odd(arr):
    even = []
    odd = []
    for item in arr:
        num = int(item)
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even, odd

user_input = input("Enter elements separated by space: ")
array = user_input.split()

even, odd = separate_even_odd(array)

print(f"Even elements in the array: {even}.")
print(f"Odd elements in the array: {odd}.")