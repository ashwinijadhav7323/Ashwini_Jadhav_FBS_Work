### Write a program to convert days into years, weeks and days.

#Take total days.
days = int(input("Enter number of days : "))

#Perform Operation 
years = days // 365
weeks = (days % 365) // 7
remaining_days = (days % 365) % 7

#Display result
print(f'From total number of days {days} there are {years}years, {weeks}weeks & {remaining_days}days.')