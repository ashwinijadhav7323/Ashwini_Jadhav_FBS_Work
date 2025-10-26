### Write a program to separate three digit number.

num = int(input("Enter three digit number: "))
n = num
 
while(n != 0):
    d = n % 10
    n = n // 10
    print(d)
    #print(n)