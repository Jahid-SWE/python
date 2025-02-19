start_number  = int(input("Enter Your start number you want : "))
ending_number  = int(input("Enter Your ending number you want : "))
even_numbers =[]
odd_numbers =[]
for i in range(start_number,ending_number):
    if i%2 ==0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)
print("Total Even number : ",even_numbers)
print("Total Odd number : ",odd_numbers)
