import re, os
from datetime import datetime
from commons import calculate_age, signup

# Username and Password hashing encryption
# def login(username, password, tries):
#     # Hash the user's password with the salt value
#     hashed_username = hashlib.sha256((salt + username[0]).encode()).hexdigest()
#     hashed_password = hashlib.sha256((salt + password).encode()).hexdigest()
#     username = username.split("@")
#     with open("texts/users.txt", "r") as file:
#         users = file.readlines()
    
#     for user in users:
#         user_data = user.strip().split(", ")
#         if user_data[0] == hashed_username and user_data[1] == username[1] and user_data[2] == hashed_password:
#             user = [username[0], username[1]]
#             return user
#         else:
#             tries += 1
#             response = ["Incorrect Username or Password, You have {tries} tries remaining!", tries]

def add_lecturer_profile(username):
    username, role = username.strip().split("@")
    name = input("Enter Name: ")
    address = input("Enter address: ")
    contact = input("Enter Contact No: ")
    email = input("Enter email: ")
    
    try:
        with open("texts/lecturers.txt", "a+") as file:
            users = file.readlines()
            if any(user.strip().split(", ")[0] == username and user.strip().split(", ")[1] == role for user in users):
                print("Lecturer Profile already exists")
                return "exists"
            file.write(f"{username}, {role}, {name}, {address}, {contact}, {email}\n")
        print("Lecturer profile added successfully")
        return "added"
    except FileNotFoundError:
        with open("texts/lecturers.txt", "w") as file:
            file.write(f"{username}, {role}, {name}, {address}, {contact}, {email}\n")
            print("Lecturer Profile added successfully")
    except PermissionError:
        print("Permission denied. Cannot access the file.")
    except Exception as e:
        print(f"Error: {e}")
    return "error"
    
def update_lecturer_profile(username):
    username, role = username.strip().split("@")
    try:
        with open("texts/lecturers.txt", "r") as file:
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
            lecturer[7] = calculate_age(lecturer[6])
            lecturer[8] = input("Enter citizenship id: ")
        else:
            exit()

        with open("texts/lecturers.txt", "w") as file:
            for lecturer in lecturers:
                file.write(", ".join(lecturer) + "\n")

    except FileNotFoundError:
        print("Lecturer Profile not found!")
    except PermissionError:
        print("Permission denied. Cannot access the file.")
    except Exception as e:
        print(f"Error: {e}")
    return "success"

def subject_topic():
    print("... Displaying Subjects...")
    topics = []
    subjects = []
    index = 1
    try:
        try:
            with open("texts/topics.txt", "r") as file:
                for line in file:
                    topic, subject = line.strip().split("@")
                    if subject not in subjects:
                        subjects.append(subject)
        except FileNotFoundError:
            print("No subjects found. Creating a new subject.")
            subject = input("Enter subject name: ")
            topic = input("Enter topic name within the subject: ")
            subjects.append(subject)
            with open("texts/topics.txt", "w") as file:
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
        with open("texts/topics.txt", "a") as file:
            for topic in topics:
                file.write(f"{topic}\n")
        print("Topic/s Registered Successfully!")
        return "success"
    except PermissionError:
        print("Permission denied. Cannot access the file.")
    except Exception as e:
        print(f"Error: {e}")

def delete_user(username):
    users = []
    lecturers = []
    username, role = username.strip().split("@")

    # Read users.txt and store the data in a list
    with open("texts/users.txt", "r") as file:
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
        with open("texts/users.txt", "w") as file:
            for user in users:
                file.write(f"{user['username']}, {user["password"]}, {user['role']}\n")

        # If the user is a lecturer, remove the corresponding line from lecturers.txt
        if user_to_delete["role"] == "lecturer":
            with open("texts/lecturers.txt", "r") as file:
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
            with open("texts/lecturers.txt", "w") as file:
                file.writelines(lecturers)
                
        print("User deleted successfully.")
        return "success"
    else:
        print("User not Deleted!")
