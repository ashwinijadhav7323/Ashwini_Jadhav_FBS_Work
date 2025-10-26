### Write a program to accept year from user to check it is a leap year or not.

y = int(input("Enter a year to check it is leap year or not :"))

if(y % 400 == 0):
    print(f'{y} is a leap year.')
elif(y % 100 == 0):
        print(f'{y} is not a leap year.')
elif (y % 4 == 0):
    print(f'{y} is a leap year.')
else:
    print(f'{y} is not a leap year.')


