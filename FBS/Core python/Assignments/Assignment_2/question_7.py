### Find the sum of three digit number.

#Take number
num = int(input("Enter three-digit number: "))

#Perform operation
a = num // 100
b = (num // 10) % 10
c = num%10

sum_digit = a+b+c
#display result
print(f'The sum of three digit number is {sum_digit}.')