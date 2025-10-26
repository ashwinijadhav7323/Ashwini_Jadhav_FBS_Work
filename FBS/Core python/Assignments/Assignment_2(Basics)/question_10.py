### Write a program to reverse three digit number.

#Take number
num1 = int(input("Enter three digit number: "))

#Perform operation
#1. Separate digit
num2 = num1
d1 = num2 % 10
num2 = num2 // 10
d2 = num2 % 10
num2 = num2 // 10
d3 = num2 % 10 
num2 = num2 // 10

#2. Reverse digit
rev = (d1*100) + (d2*10) + d3

#Display result
print(f'The reverse digits is : {rev}')