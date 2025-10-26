### Write a program to check ig given three digit number is a palindrom or not.

num = int(input("Enter three digit number to check it is palindrome or not: "))

hundreds = num // 100
tens = (num // 10) % 10
ones = num % 10

if(hundreds == ones):
    print(f'The three digit number {num} is a palindrome.')

else:
    print(f'The three digit number {num} is not a palindrome.')