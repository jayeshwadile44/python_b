#Problem Statement: Write a program that keeps asking the user to enter a password until they enter correct one.

correct_password = "secret"
while True:
    password = input("Enter password: ")
    if password == correct_password:
        print("Access granted!")
        break
    else:
        print("Incorrect password. Try again.")