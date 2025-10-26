### write a program to perform multiple choices.

ch = 0
while(ch != '7'):
    print('''Plese select option
          1. Addition
          2. Subraction
          3.Multiplication
          4. Even or odd
          5. Positive or Negative
          6. Check prime or not
          ''')
    ch = input('Enter choice: ')
    if(ch == '1'):
        print('-----------------ADDITION------------------')
        n1 = int(input("Enter number 1:"))
        n2 = int(input("Enter number 2:"))
        sum = n1 + n2
        print(f'The Addition of {n1} & {n2} is {sum}')
        print('----------------------------------------------')

    elif(ch == '2'):
        print('-----------------SUBSTRACTION------------------')
        n1 = int(input("Enter number 1:"))
        n2 = int(input("Enter number 2:"))
        sub = n1 - n2
        print(f'The Substraction of {n1} & {n2} is {sub}')
        print('----------------------------------------------')

    elif(ch == '3'):
        print('-----------------MULTIPLICATION------------------')
        n1 = int(input("Enter number 1:"))
        n2 = int(input("Enter number 2:"))
        mul = n1 * n2
        print(f'The Multiplication of {n1} & {n2} is {mul}')
        print('----------------------------------------------')

    else:
        print('Invalid Choice')