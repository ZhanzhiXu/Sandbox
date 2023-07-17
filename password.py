MINIMUM_LENGTH = 8

password = input("Please enter your password: ")
while len(password) < MINIMUM_LENGTH:
    print("Your password doesn't meet a minimum length set.")
    password = input("Please enter your password: ")

print("*" * len(password))
