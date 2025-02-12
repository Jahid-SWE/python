number = int(input("Entery your number prime or nonprime : "))
for i in range(2,number):
    if number%i == 0:
        print(f'This is {number} not a prime Numbwr')
        break
else:
    print(f'This is {number} prime number')