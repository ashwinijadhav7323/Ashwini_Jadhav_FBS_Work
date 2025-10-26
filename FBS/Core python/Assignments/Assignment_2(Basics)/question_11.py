### Write a program to accept an integer amount from user and tell mini number of notes needed for representing that amount.

#Take integer amount
amt = int(input("Enter integer amount: "))

#Perform operation
n2000 = amt // 2000
amt = amt % 2000

n500 = amt // 500
amt = amt % 500

n200 = amt // 200
amt = amt % 200

n100 = amt // 100
amt = amt % 100

n50 = amt // 50
amt = amt % 50

n20 = amt // 20
amt = amt % 20

n10 = amt // 10
amt = amt % 10

#Display result
print(f'2000 notes : {n2000}')
print(f'500 notes : {n500}')
print(f'200 notes : {n200}')
print(f'100 notes : {n100}')
print(f'50 notes : {n50}')
print(f'20 notes : {n20}')
print(f'10 notes : {n10}')