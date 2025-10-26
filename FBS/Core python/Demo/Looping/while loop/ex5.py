### addition of digits.

num = int(input("Enter three digits number to perform addition: "))
n = num
sum = 0

while(n != 0):
    d = n % 10
    n = n // 10
    sum = sum + d
    print(sum)