### Nested if else example

num = int(input("Enter Number: "))

if(num > 0):
    if(num <= 50):
        if(num <= 100):
            if(num <= 150):
                if(num <= 200):
                    print(f'Number is greater than 200')
                else:
                    print(f'Number in between 151 to 200 ')
            else:
                print(f'Number in between 101 to 150')
        else:
            print(f'Number in between 51 to 100')
    else:
        print(f'Number in between 0 to 50')
else:
    print(f'Number is less than 0')