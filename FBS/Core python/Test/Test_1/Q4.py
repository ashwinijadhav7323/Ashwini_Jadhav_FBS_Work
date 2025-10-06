### Calculate the cost of painting the following building walls (both interior & exterior). You need to accept area (onr wall) & cost of both interior & exterior wall.

#Take input from user
area_wall_1 = float(input("Enter the area of one wall: "))
num_interior_wall = int(input("Enter number of interior walls: "))
num_exterior_wall = int(input("Enter number of exterior walls: "))
cost_interior_wall = float(input("Enter cost for interior painting: "))
cost_exterior_wall = float(input("Enter cost for exterior painting: "))

#Perform operation
total_interior_cost = area_wall_1*num_interior_wall*cost_interior_wall
total_exterior_cost = area_wall_1*num_exterior_wall*cost_exterior_wall
total_cost = total_interior_cost + total_exterior_cost

#Display result
print(f'\nTotal Interior cost is {total_interior_cost}')
print(f'Total Exterior cost is {total_exterior_cost}')
print(f'Total cost for both {total_cost}')
