### Write a program to input two angles from user & find third angle of triangle.

#Take a two angles
angle_1 = int(input("Enter first angle : "))
angle_2 = int(input("Enter second angle : "))

#perform operation
angle_3 = 180 - (angle_1 + angle_2)

#Display Result
print(f'Third angle of the triangle is {angle_3}.')