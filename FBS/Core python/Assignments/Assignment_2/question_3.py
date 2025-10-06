### Convert distant given in feet & inches into meter and centimeter.

#Take feet & inches
feet = int(input("Enter distant in feet: "))
inches = int(input("Enter distant in inches: "))

#Perform operation
Total_inches = (feet*12) + inches
cm = Total_inches*2.54
meters = cm//100
Remaining_cm = cm%100

#Display result
print(f'Distant in meter is {meters}m & in centimeter is {Remaining_cm}cm')
