### Write a program to input all sides of a triangle & check whether triangle is vaild or not.

side1 = float(input("Enter side 1 of triangle: "))
side2 = float(input("Enter side 2 of triangle: "))
side3 = float(input("Enter side 3 of triangle: "))

if(side1 + side2 > side3) and (side2 + side3 > side1) and (side1 + side3 > side2):
    print(f'Triangle is valid.')
else:
    print(f'Triangle is not valid.')