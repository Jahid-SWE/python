numberOne = int(input("Enter Your First Number : "))
numberSecond = int(input("Enter Your Second Number : "))
numberThird = int(input("Enter Your third Number : "))
if numberOne>numberSecond and numberOne > numberThird:
    print(f"This First number {numberOne} is max valu among of two and three number") 
elif numberSecond > numberOne and numberSecond > numberThird:
    print(f"This second number {numberSecond} is max valu among of one and three number") 
else:
    print(f"This third number {numberThird} is max valu among of ond and two number") 
