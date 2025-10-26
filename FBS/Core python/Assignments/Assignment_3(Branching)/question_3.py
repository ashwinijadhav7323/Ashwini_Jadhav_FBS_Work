### Write a program to input angle of triangle & check whether triangle is valid or not.

angle1 = int(input("Enter angle 1 of a triangle: "))
angle2 = int(input("Enter angle 2 of a triangle: "))
angle3 = int(input("Enter angle 3 of a triangle: "))

triangle = angle1 + angle2 + angle3

if(triangle == 180):
    print(f'Triangle is valid.')
else:
    print(f'Triangle is not valid.')
