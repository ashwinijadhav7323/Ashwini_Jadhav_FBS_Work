### Write a program to input any alphabet and check whether it is vowel or consonant.

alphabet = "aeiouAEIOU"

a = input("Enter a alphabet to check it is vowel or console: ")

if(a in alphabet ):
    print(f'{a} is a vowel.')
else:
    print(f'{a} is a console.')