print("Login")
print("Please enter your email address 👇")
email = input(" ")

if email.strip() == "":
    print("Error! Email cannot be empty.")
elif not email.endswith("@gmail.com"):
    print("Email must end with @gmail.com!")
else:
    print("Enter your password:")
    password = input(" ")

    if len(password) < 8:
        print("Your password is too short! It must be at least 8 characters long.")
    else:
        print("Confirm your password:")
        password2 = input(" ")

        if password != password2:
            print("Passwords do not match.")
        else:
            print("Enter your name:")
            name = input(" ").lower()
            a = f"{name}21@gmail.com"
            b = f"{name}1@gmail.com"
            c = f"{name}34@gmail.com"
            print("\nChoose a nickname:")
            print(f"a) {a}")
            print(f"b) {b}")
            print(f"c) {c}")

            choice = input("Enter your choice (a/b/c): ").lower()

            if choice == "a":
                nickname = a
            elif choice == "b":
                nickname = b
            elif choice == "c":
                nickname = c
            else:
                nickname = None

            if nickname:
                print("\nYour Google account has been successfully created!")
                print(f"Username: {name}")
                print(f"Email: {email}")
                print(f"Nickname: {nickname}")
            else:
                print("Invalid option selected! Nickname was not chosen.")
