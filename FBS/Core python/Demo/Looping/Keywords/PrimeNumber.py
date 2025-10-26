### To check number is prime or not.

n = int(input("Enter the number to check it is prime or not: "))
for i in range(2 , n):
    if(n % i == 0):
        #print(f'{i} is divisor of {n}')
        #print(i)
        print(f'{n} is not a prime number.')
        break
else:
    print(f'{n} is a prime number.')