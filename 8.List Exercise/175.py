'''Sort even and odd elements of array separately.'''
def sort_even_odd(arr, order = 'asc'):
    even = [x for x in arr if isinstance(x, (int, float)) and x % 2 == 0]
    odd = [x for x in arr if isinstance(x, (int, float)) and x % 2 != 0]
    reverse = True if order == 'desc' else False

    even_sort = sorted(even, reverse=reverse)
    odd_sort = sorted(odd, reverse=reverse)

    return even_sort + odd_sort

user_input = input("Enter elements separated by space: ")
order = input("Enter sort order ('asc' or 'desc'): ").lower()

array = []
for item in user_input.split():
    try:
        array.append(float(item) if '.' in item else int(item))
    except ValueError:
        print(f"Skipping non-numberic item: {item}.")

result = sort_even_odd(array, order)
print(f"Sorted evens followed by sorted odd: {result}.")
