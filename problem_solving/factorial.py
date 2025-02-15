number = int(input("Enter your factorial valu : "))
fact = 1
for i in range(1, number+1):
    if number < 0:
         print(" This is not possible to Factorial")
    if number==0:
         print("This is invalid value .")
    if number>0:
        fact = fact * i
    print(fact)