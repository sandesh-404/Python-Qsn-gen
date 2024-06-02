import re
from datetime import datetime
import os

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

    with open("users.txt", "r") as file:
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
            with open("users.txt", "a+") as file:
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

# Username and Password hashing encryption
# def login(username, password, tries):
#     # Hash the user's password with the salt value
#     hashed_username = hashlib.sha256((salt + username[0]).encode()).hexdigest()
#     hashed_password = hashlib.sha256((salt + password).encode()).hexdigest()
#     username = username.split("@")
#     with open("users.txt", "r") as file:
#         users = file.readlines()
    
#     for user in users:
#         user_data = user.strip().split(", ")
#         if user_data[0] == hashed_username and user_data[1] == username[1] and user_data[2] == hashed_password:
#             user = [username[0], username[1]]
#             return user
#         else:
#             tries += 1
#             response = ["Incorrect Username or Password, You have {tries} tries remaining!", tries]

def addLecturerProfile(username):
    username, role = username.strip().split("@")
    name = input("Enter Name: ")
    address = input("Enter address: ")
    contact = input("Enter Contact No: ")
    email = input("Enter email: ")
    
    try:
        with open("lecturers.txt", "a+") as file:
            users = file.readlines()
            if any(user.strip().split(", ")[0] == username and user.strip().split(", ")[1] == role for user in users):
                print("Lecturer Profile already exists")
                return "exists"
            file.write(f"{username}, {role}, {name}, {address}, {contact}, {email}\n")
        print("Lecturer profile added successfully")
        return "added"
    except FileNotFoundError:
        with open("lecturers.txt", "w") as file:
            file.write(f"{username}, {role}, {name}, {address}, {contact}, {email}\n")
            print("Lecturer Profile added successfully")
    except PermissionError:
        print("Permission denied. Cannot access the file.")
    except Exception as e:
        print(f"Error: {e}")
    return "error"
    
def updateLecturerProfile(username):
    username, role = username.strip().split("@")
    try:
        with open("lecturers.txt", "r") as file:
            lines = file.readlines()
            lecturers = [line.strip().split(", ") for line in lines]

        if username not in [lecturer[0] for lecturer in lecturers]:
            print("Lecturer not found!")
            return

        index = [lecturer[0] for lecturer in lecturers].index(username)
        lecturer = lecturers[index]
        choice = input(f"Do you want to edit the profile of {lecturer[2]}, Username = {lecturer[0]}?").lower()
        if choice == "y":
            lecturer[1] = input("Enter Role: ")
            lecturer[2] = input("Enter Name: ")
            lecturer[3] = input("Enter address: ")
            lecturer[4] = input("Enter Contact No: ")
            lecturer[5] = input("Enter email: ")
            lecturer[6] = input("Enter your DOB(dd-mm-YYYY): ")
            lecturer[7] = calculateAge(lecturer[6])
            lecturer[8] = input("Enter citizenship id: ")
        else:
            exit()

        with open("lecturers.txt", "w") as file:
            for lecturer in lecturers:
                file.write(", ".join(lecturer) + "\n")

    except FileNotFoundError:
        print("Lecturer Profile not found!")
    except PermissionError:
        print("Permission denied. Cannot access the file.")
    except Exception as e:
        print(f"Error: {e}")
    return "success"

def subjectTopic():
    print("... Displaying Subjects...")
    topics = []
    subjects = []
    index = 1
    try:
        try:
            with open("topics.txt", "r") as file:
                for line in file:
                    topic, subject = line.strip().split("@")
                    if subject not in subjects:
                        subjects.append(subject)
        except FileNotFoundError:
            print("No subjects found. Creating a new subject.")
            subject = input("Enter subject name: ")
            topic = input("Enter topic name within the subject: ")
            subjects.append(subject)
            with open("topics.txt", "w") as file:
                file.write(f"{topic}@{subject}\n")

        for sub in subjects:
            print(f"{index}. {sub}")
            index += 1
        print("1. Add subject")
        print("2. Add Topic within Subject")
        print("3. Exit")
        choice = int(input("Choose: "))
        if choice == 1:
            subject = input("Enter subject name: ")
            if subject not in subjects:
                subjects.append(subject)
            print("Add topic for the subject(Require after creating subject).")
            topic = input("Enter topic name: ")
            topic = f"{topic}@{subject}"
            topics.append(topic)
        elif choice == 2:
            topic = input("Enter topic name: ")
            print("Choose Subjects from below")
            index = 1
            for subject in subjects:
                print(f"{index}. {subject}")
                index += 1
            choice = int(input("Enter Subject no: ")) - 1
            topic = f"{topic}@{subjects[choice]}"
            topics.append(topic)
        else:
            exit()
        with open("topics.txt", "a") as file:
            for topic in topics:
                file.write(f"{topic}\n")
        print("Topic/s Registered Successfully!")
        return "success"
    except PermissionError:
        print("Permission denied. Cannot access the file.")
    except Exception as e:
        print(f"Error: {e}")

def deleteUser(username):
    users = []
    lecturers = []
    username, role = username.strip().split("@")

    # Read users.txt and store the data in a list
    with open("users.txt", "r") as file:
        for line in file:
            user, password, role = line.strip().split(", ")
            users.append({"username": user, "password":password, "role": role})

    # Find the user to delete
    user_to_delete = None
    for user in users:
        if (user["username"] == username and user["role"] == role):
            user_to_delete = user
            break

    # Check if the user exists
    if user_to_delete is None:
        print("User not found.")
        return "notFound"

    choice = input(f"Are you sure you want to remove {username}@{role}(y/n):").lower()
    
    if choice == 'y':
        # Remove the user from the users list
        users = [user for user in users if not (user["username"]== username and user["role"]== role)]        
        # Write the updated users list to users.txt
        with open("users.txt", "w") as file:
            for user in users:
                file.write(f"{user['username']}, {user["password"]}, {user['role']}\n")

        # If the user is a lecturer, remove the corresponding line from lecturers.txt
        if user_to_delete["role"] == "lecturer":
            with open("lecturers.txt", "r") as file:
                for lecturer in lecturers:
                    lecturer = file.readlines().strip().split(", ")

            # Find the index of the line to remove
            index_to_remove = None
            for i, lecturer in enumerate(lecturers):
                if user_to_delete["username"] in lecturer:
                    index_to_remove = i
                    break

            # Remove the line from the lecturers list
            if index_to_remove is not None:
                del lecturers[index_to_remove]

            # Write the updated lecturers list to lecturers.txt
            with open("lecturers.txt", "w") as file:
                file.writelines(lecturers)
                
        print("User deleted successfully.")
        return "success"
    else:
        print("User not Deleted!")


def AdminPanel(username):
    while True:
        print("#####   ADMIN PANEL   #####")
        print(f"Welcome {username}!")
        print("You have the following choices!")
        print("1. Register new user(Lecturer/Exam Unit personnel)")
        print("2. Add Lecturer Profile")
        print("3. edit/Update Lecturer Profile")
        print("4. Add Subjects and Topics")
        print("5. Remove user(Lecturer/Exam Unit personnel)")
        print("6. Sign Out")
        try:
            choice = int(input("Choose : "))
        except:
            print("Invalid choice!")
        if choice == 1:
            while True:
                print("Available roles: \n1. Admin(admin) \n2. Lecturer(admin) \n3. EUP(eup)")
                username = input("Enter Username(user's_name@role):")
                password = input("Enter Password:")
                registered = signup(username, password)
                if registered == True:
                    break
        elif choice == 2:
            lecturer_username = input("Enter the username of the lecturer you want to add: ")
            lecturer_profile = addLecturerProfile(lecturer_username)
            if lecturer_profile == "added" or lecturer_profile == "exists":
                break
            else:
                choice = input("Try again?(y/n)").lower()
                if(choice == "n"):
                    break
        elif choice == 3:
            lecturer_username = input("Enter the username of the lecturer you want to edit/update: ")
            response = updateLecturerProfile(lecturer_username)
            if response == "success":
                break
        elif choice == 4:
            response = subjectTopic()
            if response == "success":
                break
        elif choice == 5:
            user = input("Enter username(To delete): ")
            response = deleteUser(user)
            if response == "success":
                break
        elif choice == 6:
            print("... Signing out ...")
            os.system("sleep 3")
            exit()
        else:
            print("Option not available, Try again!")

def LecturerPanel(username):
    print("#####   LECTURER PANEL   #####")
    print(f"Welcome {username}!")
    print("You have the following choices!")
    
    

def EUPPanel(username):
    print("#####   EUP PANEL   #####")
    print(f"Welcome {username}!")
    print("You have the following choices!")