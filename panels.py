from functionalities import signup, addLecturerProfile, updateLecturerProfile, subjectTopic, deleteUser
import sys, os
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