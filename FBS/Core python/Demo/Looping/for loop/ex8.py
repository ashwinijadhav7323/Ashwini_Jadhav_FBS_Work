### sum of first n numbers

n = int(input("Enter a value of n: "))
sum = 0

for i in range(1, n+1):
    sum = sum + i

print("Addition is ",sum)