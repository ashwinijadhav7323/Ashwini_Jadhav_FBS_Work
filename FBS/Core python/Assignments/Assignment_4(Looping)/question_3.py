### WAP to print sum of series upto n.

n = int(input("Enter number limit : "))
sum = 0

for i in range(1, n+1):
    sum = sum+i
print(sum)