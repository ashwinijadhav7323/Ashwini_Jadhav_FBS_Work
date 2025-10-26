### WAP to print all odd numbers until n.

n = int(input("Enter number limit : "))
print("Odd numbers are : ")

for i in range(1, n+1, 2):
    print(i, end=" ")