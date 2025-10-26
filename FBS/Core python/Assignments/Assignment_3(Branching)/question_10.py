### Write a program to check a person is eligible to marry or not.(male age>=21 & female age>=18)

male_age = int(input("Enter Age of Male: "))
female_age = int(input("Enter Age of Female: "))

if(male_age >= 21) and (female_age >= 18):
    print(f'Both are Eligible to Marry.')
elif(male_age < 21) and (female_age >= 18):
    print(f'Male is not Eligible to Marry.')
elif(male_age >= 21) and (female_age < 18):
    print(f'Female is not Eligible to Marry.')
else:
    print(f'Both are not Eligible to Marry.')