import datetime, os


def calculate_age(birthdate):
    try:
        birthdate = datetime.strptime(birthdate, "%dd-%mm-%YYYY")
        today = datetime.now()
        age = (
            today.year
            - birthdate.year
            - ((today.month, today.day) < (birthdate.month, birthdate.day))
        )
        return age
    except ValueError:
        print("Incorrect date format, should be DD-MM-YYYY")
        return None

def validate_password(password):
    errors = []
    password = password.strip()
    if len(password) < 8:
        errors.append("Your password must be at least 8 characters long.")

    if not any(char.isupper() or char.islower() for char in password):
        errors.append("Your password must include letters.")

    if not any(char.isdigit() for char in password):
        errors.append("Your password must include numbers.")

    if any(char == " " for char in password):
        errors.append("Your password must not have spaces.")

    if not any(char in '[!@#$%^&*(),.?":{}|<>]' for char in password):
        errors.append("Your password must have at least 1 symbol.")
        
    if "@" in password:
        print("Please do not use @!")

    if errors:
        print("Invalid Password!")
        for error in errors:
            print(error)
        return False
    
    return True

def login(username, password, tries):
    tries += 1

    try:
        username, role = username.strip().split("@")
    except Exception as e:
        return [False, f"Error: {e}", tries]

    with open("texts/users.txt", "r") as file:
        users = file.readlines()

    for user in users:
        user_data = user.strip().split(", ")
        if (
            user_data[0] == username
            and user_data[1] == password
            and user_data[2] == role
        ):
            tries = 1
            return [True, (username, role), tries]

    return [
        False,
        f"Incorrect Username or Password, You have {3-tries} tries remaining!",
        tries,
    ]

def validate_username(username):
    if len(username.split(" ")) != 1:
        print("... Invalid Username! Your username must be a single word! ...")
        return False
    else:
        return True 

def signup(username, password):
    try:
        username, role = username.strip().split("@")
    except Exception as e:
        return [False, f"Error: {e}"]
    valid_username = validate_username(username)
    valid_password = validate_password(password)
    if valid_password == True and valid_username == True:
        try:
            with open("texts/users.txt", "a+") as file:
                users = file.readlines()
                if any(
                    user.strip().split(", ")[0] == username
                    and user.strip().split(", ")[1] == role
                    for user in users
                ):
                    print("... User already exists ...")
                    print("Exiting...")
                    os.system("sleep 3")
                    os.system("clear")
                    return
                file.write(f"{username}, {password}, {role}\n")
                print("... User added successfully ...")
                print("Exiting...")
                os.system("sleep 3")
                os.system("clear")
        except FileNotFoundError:
            with open("users.txt", "w") as file:
                file.write(f"{username}, {password}, {role}\n")
                print("... User added successfully ...")
                print("Exiting...")
                os.system("sleep 3")
                os.system("clear")
        except PermissionError:
            print("... Permission denied. Cannot access the file ...")
            print("Exiting...")
            os.system("sleep 3")
            os.system("clear")
        except Exception as e:
            print(f"Error: {e}")
            print("Exiting...")
            os.system("sleep 3")
            os.system("clear")
        return True
    else:
        return False


def change_password(username):
    try:
        password = input("Enter old password: ")
        while True:
            # Take the username and password from users.txt and compare username and password
            with open("texts/users.txt", "r") as file:
                users = file.readlines()
                for user in users:
                    user_data = user.strip().split(", ")
                    if user_data[0] == username and user_data[1] == password:
                        new_password = input("Enter new password: ").strip()
                        if validate_password(new_password):
                            # Replace the old password with the new one
                            new_user_data = f"{username}, {new_password}, {user_data[2]}\n"
                            users[users.index(user)] = new_user_data
                            # Write the updated user data back to the file
                            with open("texts/users.txt", "w") as file:
                                file.writelines(users)
                            print("... Password changed successfully ...")
                            return
                        else:
                            print("Invalid new password. Password not changed.")
                            print("Exiting...")
                            os.system("sleep 3")
                            os.system("clear")
                        return
                print("Username or password is incorrect. Password not changed.")
                quit = input("Do you want to quit, Yes = q").lower()
                if quit == "q":
                    break
    except FileNotFoundError:
        print("users.txt file not found.")
