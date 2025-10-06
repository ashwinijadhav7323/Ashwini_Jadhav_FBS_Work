### WAP to calculate selling price of book based on cost price and discount.

#Take a cost price & discount
cost_price = float(input("Enter cost price: "))
discount = float(input("Enter discount: "))

#Perform operation
selling_price = cost_price - (discount*cost_price)/100

#Display result
print(f'Selling price of book is {selling_price}')