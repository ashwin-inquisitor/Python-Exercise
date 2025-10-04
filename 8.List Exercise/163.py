'''Copy all elements from an array to another array.'''
def smart_convert(value):
    if value.isdigit():
        return int(value)
    elif value.startswith('-') and value[1:].isdigit():
        return int(value)
    elif value.count('.') == 1 and value.replace('.','',1).isdigit():
          return float(value)
    elif value.startswith('-') and value[1:].count('.') == 1 and value[1:].replace('.', '', 1).isdigit():
        return float(value)
    else:
        return value


try:
    user_input = input("Enter elements separated by space: ")
    original_array = [smart_convert(item) for item in user_input.split()]

    copied_array = original_array[:]

    print(f"Original array: {original_array}.")
    print(f"Copied array: {copied_array}.")
except Exception as e:
    print(f"Something went wrong: {e}.")