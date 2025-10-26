### WAP to calculate area of triangle and rectangle.

#Take l & b for triangle and rectangle.
l1 = float(input("Enter length of triangle: "))
b1 = float(input("Enter breadth of triangle: "))
l2 = float(input("Enter length of rectangle: "))
b2 = float(input("Enter breadth of rectangle: "))

#Perform operation
area_of_triangle = (1/2)*l1*b1
area_of_rectangle = l2*b2

#Display result
print(f'Area of triangle is {area_of_triangle} & area of rectangle is {area_of_rectangle}')