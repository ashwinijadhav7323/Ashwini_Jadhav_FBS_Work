### Write a peogram to find area & perimeter of following fig.(Accept the length, breadth & radius from user.)

L = int(input("Enter length: "))
B = int(input("Enter breadth: "))

Area = (L*B) + 3.14*(B**2)/8
Perimeter = (2*L) + B + 3.14*(B/2) 

print(f'Area of given fig. is {Area} & Perimeter of given fig. is {Perimeter}')