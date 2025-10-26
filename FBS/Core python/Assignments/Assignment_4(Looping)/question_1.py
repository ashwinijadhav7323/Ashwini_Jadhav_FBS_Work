### WAP to print all even numbers until n.

n = int(input("Enter the limit: "))
print("Even numbers are : ")

for i in range(2, 1+n, 2):
    print(i, end=" ")