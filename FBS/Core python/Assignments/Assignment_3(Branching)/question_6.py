### Write a program to calculate profit and loss.

Selling_price = int(input("Enter selling price: "))
Cost_price = int(input("Enter cost price: "))

profit = Selling_price - Cost_price
loss = Cost_price - Selling_price

if(Selling_price > Cost_price):
    print(f'We got profit of Rs.{profit}')
elif(Cost_price > Selling_price):
    print(f'We have loss of Rs.{loss}')
else:
    print(f'No profit, No loss.')
