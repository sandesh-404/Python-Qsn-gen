import datetime, re
def calculateAge(birthdate):
    try:
        birthdate = datetime.strptime(birthdate, "%dd-%mm-%YYYY")
        today = datetime.now()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age
    except ValueError:
        print("Incorrect date format, should be DD-MM-YYYY")
        return None

def validate_password(password):
    if len(password) < 8:
        print("Invalid Password! Your password must be at least 8 characters long!")
        return False

    if not re.search(r'[a-zA-Z]', password):
        print("Invalid Password! Your password must include letters!")
        return False

    if not re.search(r'\d', password):
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
        if user_data[0] == username and user_data[1] == password and user_data[2] == role:
            tries = 1
            return [True, (username, role), tries]

    return [False, f"Incorrect Username or Password, You have {3-tries} tries remaining!", tries]

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
                if any(user.strip().split(", ")[0] == username and user.strip().split(", ")[1] == role for user in users):
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