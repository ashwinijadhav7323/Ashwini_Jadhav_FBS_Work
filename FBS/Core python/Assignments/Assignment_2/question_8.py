### Write a program to swap two numbers using third variable

#Take x & y
x = int(input("Enter value of x: "))
y = int(input("Enter value of y: "))

print(f'Value of x & y before swap {x} & {y}')

#Perform operation
z = x
x = y
y = z

#Display result
print(f'Value of x & y after swap is {x} & {y}')
