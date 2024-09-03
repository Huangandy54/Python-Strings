# Objective:
# The aim of this assignment is to process and format user input data.

# Task 1: Input Length Validator
# Write a script that checks the length of the user's first name and last name. Both should be at least 2 characters long. If not, print an error message.

while True:
    first_name=input("First Name: ")
    if len(first_name) >= 2:
        break
    else:
        print("Error: Minimum 2 Characters required. Try again")

while True:
    last_name=input("Last Name: ")
    if len(last_name) >= 2:
        break
    else:
        print("Error: Minimum 2 Characters required. Try again")

# Task 2: Password Complexity Checker
# Create a function that checks the complexity of a user's password. The password must be at least 8 characters long, contain one uppercase letter, one lowercase letter, and one number. If the password does not meet these criteria, print a message explaining the complexity requirements.

def password_checker(password):
    upper, lower, number = False , False, False
    if len(password) < 8:
        print("Error: Password needs to contain at least 8 characters")
    for character in password:
        if not upper and character.isupper():
            upper = True
        elif not lower and character.islower():
            lower = True
        elif not number and character.isdigit():
            number = True
    if not upper:
        print("Error: Password needs to contain an uppercase letter")
    if not lower:
        print("Error: Password needs to contain an lowercase letter")
    if not number:
        print("Error: Password needs to contain at least one number")
    
    if upper and lower and number:
        return True
    else:
        return False

password=input("Enter a password")
if password_checker(password):
    print("Valid Password")

# Task 3: Email Formatter
# Implement a script that ensures all user email addresses are in a standard format

def email_checker(email):
    if "@" in email and "." in email:
        return True
    else:
        return False 
    
email=input("Enter an email")
if email_checker(email):
    print("Valid Email")
else:
    print("Invalid Email")