'''input number from user and check whether the number is even or odd using switch case. '''

num = int(input("Enter a number: "))

match num % 2:
    case 0:
        print(str(num)+" is even.")
    case 1:
        print(str(num)+ " is odd")
    case _:
        print("Unexpected input.")