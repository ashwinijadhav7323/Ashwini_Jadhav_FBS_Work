### Write a program to check uerid & password is matched or not.

id = "Ashwini"
p = 7323

user_id = input("Enter id for login: ")
password = input("Enter password: ") 

if(id == user_id and p == password):
    print(f'\n----Login Id & Password is matched----')
else:
    print(f'\n----Login Id & Password is not matched-----')  

