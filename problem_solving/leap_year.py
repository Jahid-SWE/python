year = int(input("Enter your expected year : "))

if year%4 == 0 and year%100 !=0:
    print(f"This is a {year} leap year")
elif year%100 == 0 and year%400 == 0:
    print(f"This is a {year} leap Year ")
else:
    print(f"This is {year} Not leap Year")