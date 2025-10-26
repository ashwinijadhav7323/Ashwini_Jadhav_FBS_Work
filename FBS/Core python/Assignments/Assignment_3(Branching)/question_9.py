### Input 5 subject marks from user & display grade (e.g.,first class, second class,...)

sub1 = int(input("Enter marks of subject 1: "))
sub2 = int(input("Enter marks of subject 2: "))
sub3 = int(input("Enter marks of subject 3: "))
sub4 = int(input("Enter marks of subject 4: "))
sub5 = int(input("Enter marks of subject 5: "))

total_marks = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total_marks/500)*100

print(f'\nTotal marks of all subject is {total_marks}')
print(f'Percentage is {percentage}%')

if(percentage >= 90):
    print(f'\nGrade : A+')
elif(percentage >= 80):
    print(f'\nGrade : A')
elif(percentage >= 70):
    print(f'\nGrade : B+')
elif(percentage >= 60):
    print(f'\nGrade : B')
elif(percentage >= 50):
    print(f'\nGrade : C')
elif(percentage >= 40):
    print(f'\nGrade : D')
else:
    print(f'\nFail')