### Write a program to enter P,R,T & calculate Compound Interest

#Take value of P,R,T
P = int(input("Enter Principal value : "))
R = int(input("Enter Rate of Interest : "))
T = int(input("Enter Time taken : ")) 

#Perform Operation
CI = P * ((1 + (R/100)) ** T) - P

#Display Result
print(f'The Compound Interest is {CI}.')