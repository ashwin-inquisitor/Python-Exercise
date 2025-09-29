'''Read and print elements of array.(using recursion.)'''
def print_list_recursive(lst, index = 0 ):
    if index == len(lst):
        return
    print(f"Element {index}: {lst[index]}")
    print_list_recursive(lst, index + 1)

try:
    user_input = input("Enter list of elements separated by spaces: ")
    user_list = user_input.split()
    print("\nPrinting list of elements recursively: ")
    print_list_recursive(user_list)
except Exception as e:
    print(f"Unexpected error: {e}")