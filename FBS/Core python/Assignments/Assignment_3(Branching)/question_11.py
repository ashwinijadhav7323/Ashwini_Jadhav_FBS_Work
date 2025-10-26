### Accept age of 5 people & also per person ticket amount & then calculate total amount to ticket to travel for all of them based on following condition.
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Other need to pay full.

total_amount = 0

#Person1
age1 = int(input("Enter age of person 1: "))
ticket1 = int(input("Enter Ticket amount: "))

if(age1 > 12):
    final1 = ticket1 - (0.30 * ticket1)
elif (age1 > 59):
    final1 = ticket1 - (0.50 * ticket1)
else:
    final1 = ticket1

total_amount += final1

#Person2
age2 = int(input("Enter age of person 2: "))
ticket2 = int(input("Enter Ticket amount: "))

if(age2 > 12):
    final2 = ticket2 - (0.30 * ticket2)
elif (age2 > 59):
    final2 = ticket2 - (0.50 * ticket2)
else:
    final2 = ticket2

total_amount += final2

#Person3
age3 = int(input("Enter age of person 3: "))
ticket3 = int(input("Enter Ticket amount: "))

if(age3 > 12):
    final3 = ticket3 - (0.30 * ticket3)
elif(age3 > 59):
    final3 = ticket3 - (0.50 * ticket3)
else:
    final3 = ticket3

total_amount += final3

#Person4
age4 = int(input("Enter age of person 4: "))
ticket4 = int(input("Enter Ticket amount: "))

if(age4 > 12):
    final4 = ticket4 - (0.30 * ticket4)
elif(age4 > 59):
    final4 = ticket4 - (0.50 * ticket4)
else:
    final4 = ticket4

total_amount += final4

#Person5
age5 = int(input("Enter age of person 5: "))
ticket5 = int(input("Enter Ticket amount: "))

if(age5 > 12):
    final5 = ticket5 - (0.30 * ticket5)
elif(age5 > 59):
    final5 = ticket5 - (0.50 * ticket5)
else:
    final5 = ticket5

total_amount += final5

print(f'\nTotal travel amount for all 5 persons are {total_amount}')