### Write a program to enter P,T,R  and calculate Simple Interest.

#Take a value P,R,T
P = int(input("Enter Principal value : "))
R = int(input("Enter Rate of Interest : "))
T = int(input("Enter Time taken : ")) 

#Perform Operation
SI = (P * R * T) / 100

#Display Result
print(f'The Simple Interest is {SI}')