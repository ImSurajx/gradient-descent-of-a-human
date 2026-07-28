"""
# Bonus Challenge

## Problem 19 - About Me

Create a small program that asks the user for at least **10 different details.**

Example

- Name
- Age
- Phone Number
- Email
- Address
- City
- State
- Country
- Favourite Language
- Hobby

Print everything in a professional-looking format.
=========================
        PROFILE
=========================

Name   : Suraj
Age    : 20
Height : 170 cm
Weight : 65 kg

=========================

"""
name = input("enter your name: ")
age = int(input("enter your age: "))
phone_number = int(input("enter your number: "))
email = input("enter your email: ")
address = input("enter your address: ")
city = input("enter your city: ")
state = input("enter your state: ")
country = input("enter your country: ")
fav_lang = input("enter your favourite language: ")
hobby = input("enter your hobby: ")
print(f"""
==============================
         MY PROFILE
==============================

Name               : {name}
Age                : {age}
Phone Number       : {phone_number}
Email              : {email}
Address            : {address}
City               : {city}
State              : {state}
Country            : {country}
Favourite Language : {fav_lang}
Hobby              : {hobby}

==============================
""")