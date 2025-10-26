### A man goes for shopping. He buys 5 product. Accept the price of all product and display the total bill after adding 18% GST.

p1 = int(input("Enter the price of first product: "))
p2 = int(input("Enter the price of second product: "))
p3 = int(input("Enter the price of third product: "))
p4 = int(input("Enter the price of fourth product: "))
p5 = int(input("Enter the price of fifth product: "))

total = p1 + p2 + p3 + p4 + p5
total_bill = total * 1.18

print(f'Total bill of all 5 products including 18% GST is {total_bill}')
