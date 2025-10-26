### Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

side1 = float(input("Enter side 1 of triangle: "))
side2 = float(input("Enter side 2 of triangle: "))
side3 = float(input("Enter side 3 of triangle: "))

if(side1 + side2 > side3) and (side2 + side3 > side1) and (side1 + side3 > side2):
    print(f'Triangle is valid.')
    if(side1 == side2 == side3):
        print(f'Triangle is an equilateral triangle.')
    else:
        if(side1 == side2) or (side2 == side3) or (side1 == side3):
            print(f'Triangle is an isosceles triangle.')
        else:
            print(f'Triangle is a scalene triangle.')
else:
    print(f'Triangle is not valid.')