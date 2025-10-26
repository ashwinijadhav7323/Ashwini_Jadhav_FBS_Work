### Write a program to input electricity unit charges & calculate total electricity bill according to the given condition:
#1. For first 50 units Rs. 0.50/unit
#2. For next 100 units Rs. 0.75/unit
#3. For next 100 units Rs. 1.20/unit
#4. For unit above 200 Rs. 1.50/unit
#An additional surcharge of 20% is added to the bill

units = int(input("Enter the electricity unit : "))
amt = 0

if(units > 0):
    if(units > 50):
        if(units > 150):
            if(units > 250):
                if(units > 450):
                    pass
                else:
                    amt = 50 * 0.5 + 100 * 0.75 + 100 * 1.20 + (units - 250) * 1.50
            else:
                amt = 50 * 0.5 + 100 * 0.75 + (units - 150) * 1.20
        else:
            amt = 50 * 0.5 + (units - 50) * 0.75
    else:
        amt = units * 0.5
else:
    amt = 0

print(amt * 1.20)


