### WAP to calculate total salary of employee based on basic, da=10% of basic, ta=12% of basic, hra=15% of basic.

#Given DA = 10%, TA=12%, HRA=15%
basic_salary = float(input("Enter basic salary of employess: "))

#Perform operation
DA = (10/100) * basic_salary
TA = (12/100) * basic_salary
HRA = (15/100) * basic_salary

total_salary = basic_salary + DA + TA + HRA

#Display result
print(f'Total salary of Employee is {total_salary}')