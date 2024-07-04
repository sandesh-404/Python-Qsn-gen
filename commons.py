import datetime, re


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
    if len(password) < 8:
        print("Invalid Password! Your password must be at least 8 characters long!")
        return False

    if not re.search(r"[a-zA-Z]", password):
        print("Invalid Password! Your password must include letters!")
        return False

    if not re.search(r"\d", password):
        print("Invalid Password! Your password must not have spaces")
        return False

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        print("Invalid Password! Your password must have at least 1 symbol!")
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


def signup(username, password):
    try:
        username, role = username.strip().split("@")
    except Exception as e:
        return [False, f"Error: {e}"]
    valid_password = validate_password(password)
    if valid_password == True:
        try:
            with open("texts/users.txt", "a+") as file:
                users = file.readlines()
                if any(
                    user.strip().split(", ")[0] == username
                    and user.strip().split(", ")[1] == role
                    for user in users
                ):
                    print("User already exists")
                    return
                file.write(f"{username}, {password}, {role}\n")
                print("User added successfully")
        except FileNotFoundError:
            with open("users.txt", "w") as file:
                file.write(f"{username}, {password}, {role}\n")
                print("User added successfully")
        except PermissionError:
            print("Permission denied. Cannot access the file.")
        except Exception as e:
            print(f"Error: {e}")
        return True
    else:
        return False


def change_password(username, password):
    try:
        # Take the username and password from users.txt and compare username and password
        with open("texts/users.txt", "r") as file:
            users = file.readlines()
            for user in users:
                user_data = user.strip().split(", ")
                if user_data[0] == username and user_data[1] == password:
                    new_password = input("Enter new password: ")
                    if validate_password(new_password):
                        # Replace the old password with the new one
                        new_user_data = f"{username}, {new_password}, {user_data[2]}\n"
                        users[users.index(user)] = new_user_data
                        # Write the updated user data back to the file
                        with open("texts/users.txt", "w") as file:
                            file.writelines(users)
                        print("Password changed successfully")
                        return
                    else:
                        print("Invalid new password. Password not changed.")
                    return
            print("Username or password is incorrect. Password not changed.")
    except FileNotFoundError:
        print("users.txt file not found.")
