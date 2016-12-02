number = int(input("Enter a number:"))

# prime numbers are greater than 1
if number > 1:
   # looks through the factor for your selected number
   for i in range(2,number):
       if (number % i) == 0:
           print(number,"is NOT a prime number")
           break
   else:
       print(number,"IS a prime number")
       

