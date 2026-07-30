"""
## Problem 14 - Login System

Store the following values inside variables.

```
Username : admin
Password : python123
```

Ask the user for username and password.

Rules:

- If the username is correct, then check the password.
- If both are correct, print:

```
Login Successful
```

- If the password is incorrect, print:

```
Incorrect Password
```

- If the username is incorrect, print:

```
Invalid Username
```
"""
username = "admin"
password = "python123"

enter_user_details = input("enter your username: ")
enter_password_details = input("enter your password: ")

if username == enter_user_details:
    if password == enter_password_details:
        print("login sucessfully.")
    else:
        print("incorrect password.")
else:
    print("invalid username.")