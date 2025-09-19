'''Display all list elements using recursion.'''
def display_list(lst, index=0):
    if index >= len(lst):
        return
    print(lst[index])
    display_list(lst, index + 1)

try:
    elements = input("Enter list of elements separated by spaces: ").split()
    print("List elements are: ")
    display_list(elements)
except Exception as e:
    print(f"Enter: {e}")