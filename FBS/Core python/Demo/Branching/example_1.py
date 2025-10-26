### Nested if else example

num = int(input("Enter Number: "))

if(num > 0):
    if(num <= 50):
        print(f'Number is in between 0 to 50')
    else:
        if(num <= 100):
            print(f'Number is in between 51 to 100')
        else:
            if(num <= 150):
                print(f'Number is in between 101 to 150')
            else:
                if(num <= 200):
                    print(f'Number is in between 151 to 200')
                else:
                    print(f'Number is greater than 201')
else:
    print(f'Number is less than 0')