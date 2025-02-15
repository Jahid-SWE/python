lower_number = int(input("Enter your lower Number : "))
upper_number = int(input("Enter your upper  Number : "))

for num in range(lower_number, upper_number + 1):
    if num > 1:
        for i in range(2,num):
            if num%i  == 0:
                break
            
        else:
            print(num, end=',')