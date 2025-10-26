### Write a program to check if user has entered correct userid and password.

userid = "Ashwinijadhav"
password = "Ash@123"

user_id = input("Enter your user id: ")
user_pass = input("Enter your password: ")

if(userid == user_id) and (password == user_pass):
    print(f'\n----------Login Successfully-------------')
else:
    print(f'\nIncorrect user id or password.')