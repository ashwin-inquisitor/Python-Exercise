'''input amount from user and print minimum number of notes 
(Rs. 500, 100, 50, 20, 10, 5, 2, 1) required for the amount.'''

amt = int(input("Enter a amount : "))

if amt >= 500:
    n500 = amt // 500
    print(f"500 * {n500}")
    amt = amt % 500
else:
    n500 = 0

if amt >= 100:
    n100 = amt // 100
    print(f"100 * {n100}")
    amt = amt % 100
else:
    n100 = 0
    
if amt >= 50:
    n50 = amt // 50
    print(f"50 * {n50}")
    amt = amt % 50
else:
    n50 = 0
    
if amt >= 20:
    n20 = amt // 20
    print(f"20 * {n20}")
    amt = amt % 20
else:
    n20 = 0
    
if amt >= 10:
    n10 = amt // 10
    print(f"10 * {n10}")
    amt = amt % 10
else:
    n10 = 0
    
if amt >= 5:
    n5 = amt // 5
    print(f"5 * {n5}")
    amt = amt % 5
else:
    n5 = 0

if amt >= 2:
    n2 = amt // 2
    print(f"2 * {n2}")
    amt = amt % 2
else:
    n2 = 0

if amt >= 1:
    n1 = amt // 1
    print(f"1 * {n1}")
    amt = amt % 1
else:
    n1 = 0