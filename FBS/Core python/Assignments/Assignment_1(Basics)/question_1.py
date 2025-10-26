### Write a program to calculate the percentage of student based on marks of any 5 subjects.

#Take marks of student
m1 = int(input("Enter marks of sub1 :"))
m2 = int(input("Enter marks of sub2 :"))
m3 = int(input("Enter marks of sub3 :"))
m4 = int(input("Enter marks of sub4 :"))
m5 = int(input("Enter marks of sub5 :"))

#Perform Operation
gain_marks = m1 + m2 + m3+ m4 + m5
percentage = (gain_marks / 500)*100

#Display Result
print(f'Percentage of Student is {percentage}%')