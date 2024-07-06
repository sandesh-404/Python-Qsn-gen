import sys, os
from panels import admin_panel, lecturer_panel, eup_panel
from commons import login

print("### Welcome to the Test Question Management System ###")

# # Import the hashlib module for password hashing
# import hashlib

# # Define a salt value for password hashing
# salt = "mysecretkey"
# tries = 0
# while True:
#     username = input("Enter your Username:")
#     password = input("Enter your Password:")
#     isLoggedIn, username, role = login(username, password, tries)

#     if isLoggedIn == True:
#         if role == "admin":
#             AdminPanel(username)
#         elif role == "lecturer":
#             LecturerPanel(username)
#         elif role == "eup":
#             EUPPanel(username)
#         else:
#             print("You have no tasks available for the given role")
#             exit()
        
#     elif isLoggedIn == False:
#         print(username)
#         if role == 4:
#             print("You have already tried 3 times, Exiting ...")
#             os.system("sleep 3")
#             sys.exit()
def main():
    tries = 0
    while tries < 3:
        username = input("Enter your Username:")
        password = input("Enter your Password:")
        isLoggedIn, message, tries = login(username, password, tries)

        if isLoggedIn is True:
            username, role = message
            if role == "admin":
                admin_panel(username)
            elif role == "lecturer":
                lecturer_panel(username)
            elif role == "eup":
                eup_panel(username)
            else:
                print("You have no tasks available for the given role")
                exit()
        else:
            print(message)
    else:
        print("You have already tried 3 times, Exiting ...")
        os.system("sleep 3")
        sys.exit()


    # username = input("Enter your Username:")
    # password = input("Enter your Password:")
    # signup(username, password)

if __name__ == "__main__":
    main()