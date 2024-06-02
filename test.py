import sys, os

def login(username, password, tries):
    tries += 1
    # try:
    username, role = username.split("@")
    print(username, role)
    # except Exception as e:
    #     return [False, f"Error: {e}", tries]

    with open("users.txt", "r") as file:
        users = [user.strip().split(", ") for user in file.readlines()]

    for user in users:
        if user[0].strip() == username and user[1].strip() == role and user[2].strip() == password:
            return [True, (username, role), tries]
    return [False, (f"Incorrect Username or Password, You have {3-tries} tries remaining!", role), tries]

def signup(username, password):
    username, role = username.strip().split("@")

    try:
        with open("users.txt", "a+") as file:
            users = file.readlines()
            if any(user.strip().split(", ")[0] == username and user.strip().split(", ")[1] == role for user in users):
                print("User already exists")
                return
            file.write(f"{username}, {role}, {password}\n")
            print("User added successfully")
    except FileNotFoundError:
        with open("users.txt", "w") as file:
            file.write(f"{username}, {role}, {password}\n")
            print("User added successfully")
    except PermissionError:
        print("Permission denied. Cannot access the file.")
    except Exception as e:
        print(f"Error: {e}")

def AdminPanel(username):
    print("#####   ADMIN PANEL #####")
    print(f"Welcome {username}!")
    print("You have the following choices!")

def LecturerPanel(username):
    print("#####   LECTURER PANEL #####")
    print(f"Welcome {username}!")
    print("You have the following choices!")

def EUPPanel(username):
    print("#####   EUP PANEL #####")
    print(f"Welcome {username}!")
    print("You have the following choices!")

def main():
    tries = 0
    while tries < 3:
        username = input("Enter your Username:")
        password = input("Enter your Password:")
        isLoggedIn, message, tries = login(username, password, tries)

        if isLoggedIn:
            username, role = message
            if role == "admin":
                AdminPanel(username)
            elif role == "lecturer":
                LecturerPanel(username)
            elif role == "eup":
                EUPPanel(username)
            else:
                print("You have no tasks available for the given role")
                exit()
        else:
            print(message)
    else:
        print("You have already tried 3 times, Exiting...")
        os.system("sleep 3")
        sys.exit()

if __name__ == "__main__":
    main()