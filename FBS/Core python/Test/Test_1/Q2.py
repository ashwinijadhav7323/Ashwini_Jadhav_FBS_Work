### Write a program to calculate simple interest based on principal, rate & time.

P = float(input("Enter Principal value: "))
R = float(input("Enter Rate of interest:"))
T = float(input("Enter Time taken: "))

SI = (P*R*T)/100

print(f'Simple interest is {SI}%')
