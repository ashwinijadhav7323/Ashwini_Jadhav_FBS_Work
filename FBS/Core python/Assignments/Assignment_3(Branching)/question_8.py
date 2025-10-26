### Write a program to prompt user to enter uerid & password. 
# After verifying the userid and password display a 4 digit random number and ask user to enter the same.
# If user enters the same number then show him success message otherwise failed.(Something like capcha)

userid = "Ashwini123"
password = "Ash@123"
random_no = "8323"

user_Id = input("Enter User Id: ")
user_pass = input("Enter Password: ")

if(userid == user_Id) and (password == user_pass):
    print(f'\n----Correct User Id & Password------')
    print(f'{random_no}')
    number = input("Enter above capcha: ")
    if(random_no == number):
        print(f'\n-------Login Successfully------------')
    else:
        print(f'\n---------Incorrect Capcha-------------')
else:
    print(f'\nIncorrect user id or password.')