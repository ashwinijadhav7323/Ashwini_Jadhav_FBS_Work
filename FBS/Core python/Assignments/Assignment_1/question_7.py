### Program to find the root of a quadratic equation.

#Take the value of a, b, c.
a = float(input("Enter value of a : "))
b = float(input("Enter value of b : "))
c = float(input("Enter value of c : "))

#Perform operation
D = b**2 - 4*a*c 
root_1 = (-b + D**0.5 ) / (2*a)
root_2 = (-b - D**0.5 ) / (2*a)

#Display result
print(f'The root of quadratic equation are : {root_1} & {root_2}')