'''Count frequency of each element in an array.'''

try:
    user_input = input("Enter elements separated by space: ")
    array = user_input.split()

    frequency = {}
    for item in array:
        frequency[item] = frequency.get(item, 0) + 1

    print("Frequency of each element: ")
    for key, value in frequency.items():
        print(f"{key}:{value}.")
except Exception as e:
    print(f"Something went wrong {e}.")