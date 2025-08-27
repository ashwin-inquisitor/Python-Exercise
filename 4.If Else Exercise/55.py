'''input cost price and selling price of a product 
and check profit or loss. Also calculate 
total profit or loss using if else.'''

cp = int(input("Enter cost price : "))
sp = int(input("Enter selling price : "))

if cp > sp:
    amt = cp - sp
    print("Loss = "+str(amt))
elif cp < sp:
    amt = sp - cp
    print("Profit ="+str(amt))
else:
    print("No profit NO loss")