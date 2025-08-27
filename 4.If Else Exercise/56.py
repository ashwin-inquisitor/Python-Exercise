'''input marks of five subjects Physics, Chemistry, Biology, 
Mathematics and Computer, calculate percentage 
and grade according to given conditions:
If percentage >= 90% : Grade A
If percentage >= 80% : Grade B
If percentage >= 70% : Grade C
If percentage >= 60% : Grade D
If percentage >= 40% : Grade E
If percentage < 40% : Grade F.'''

Phy = int(input("Enter the marks for Physics: "))
Chem = int(input("Enter the marks for Chemistry: "))
Bio = int(input("Enter the marks for Biology: "))
Math = int(input("Enter the marks for Mathematics: "))
Comp = int(input("Enter the marks for Computer: "))

total = Phy + Chem + Bio + Math + Comp
percentage = (total / 500) * 100

if percentage >= 90:
    print("Grade A")
elif percentage >= 80:
    print("Grade B")
elif percentage >= 70:
    print("Grade C")
elif percentage >= 60:
    print("Grade D")
elif percentage >= 50:
    print("Grade E")
elif percentage >= 40:
    print("Grade F")