from random import *

user_pass = input(" şifreni gir:" )
password = ('a', 'b', 'c','ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'ö', 'p', 'r', 's', 'ş', 't', 'u', 'ü', 'v', 'y',
            'z', 'w', 'x', 'y')
guess = ""

while (guess != user_pass):
    guess = ""
    for letter in range(len(user_pass)):
        guess_letter = password[randint(0, 25)]
        guess = str(guess_letter) + str(guess)
    print(guess)
print("şifreniz: ", guess)
    
