import sys, os
from commons import change_password
from admin import (
    signup,
    add_lecturer_profile,
    update_lecturer_profile,
    subject_topic,
    delete_user,
)
from lecturer import (
    add_question_answers,
    edit_question_answers,
    view_question_answers,
    delete_question_answers,
)
from eup import (
    create_question_papers,
    view_question_papers,
    add_questions_to_exam_papers,
    edit_question_papers,
)


def admin_panel(username):
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
                print(
                    "Available roles: \n1. Admin(admin) \n2. Lecturer(admin) \n3. EUP(eup)"
                )
                username = input("Enter Username(user's_name@role):")
                password = input("Enter Password:")
                registered = signup(username, password)
                if registered == True:
                    break
        elif choice == 2:
            lecturer_username = input(
                "Enter the username of the lecturer you want to add: "
            )
            lecturer_profile = add_lecturer_profile(lecturer_username)
            if lecturer_profile == "added" or lecturer_profile == "exists":
                break
            else:
                choice = input("Try again?(y/n)").lower()
                if choice == "n":
                    break
        elif choice == 3:
            lecturer_username = input(
                "Enter the username of the lecturer you want to edit/update: "
            )
            response = update_lecturer_profile(lecturer_username)
            if response == "success":
                break
            else:
                choice = input("Try again?(y/n)").lower()
                if choice == "n":
                    break
        elif choice == 4:
            response = subject_topic()
            if response == "success":
                break
            else:
                choice = input("Try again?(y/n)").lower()
                if choice == "n":
                    break
        elif choice == 5:
            user = input("Enter username(To delete): ")
            response = delete_user(user)
            if response == "success":
                break
            else:
                choice = input("Try again?(y/n)").lower()
                if choice == "n":
                    break
        elif choice == 6:
            print("... Signing out ...")
            os.system("sleep 3")
            exit()
        else:
            print("Option not available, Try again!")


def lecturer_panel(username):
    while True:
        print("#####   LECTURER PANEL   #####")
        print(f"Welcome {username}!")
        print("You have the following choices!")
        print("1. Change username and password!")
        print("2. Add new questions and answers")
        print("3. Modify/Edit/Update questions and answers")
        print("4. View Questions and answers")
        print("5. Delete Questions and answers")
        print("q. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            response = change_password(username)
        elif choice == "2":
            response = add_question_answers(username)
            if response == True:
                print("Questions added Successfully!")
            else:
                choice = input("Try again?(y/n)").lower()
                if choice == "n":
                    break
        elif choice == "3":
            response = edit_question_answers(username)
            if response == True:
                print("Questions updated Successfully!")
            else:
                choice = input("Try again?(y/n)").lower()
                if choice == "n":
                    break
        elif choice == "4":
            response = view_question_answers(username)
            if response == True:
                print("Questions displayed Successfully!")
            else:
                choice = input("Try again?(y/n)").lower()
                if choice == "n":
                    break
        elif choice == "5":
            response = delete_question_answers(username)
            if response == True:
                print("Questions deleted Successfully!")
            else:
                choice = input("Try again?(y/n)").lower()
                if choice == "n":
                    break
        elif choice == "q":
            print("... Exiting ...")
            os.system("sleep 3")
            os.system("clear")
            exit()
        else:
            print(f"Option {choice} not available, Try again!")


def eup_panel(username):
    while True:
        print("#####   EUP PANEL   #####")
        print(f"Welcome {username}!")
        print("You have the following choices!")
        print("1. Change username and password!")
        print("2. Create exam question papers")
        print("3. Add questions to Exam Papers")
        print("4. Modify/Update/Edit question papers")
        print("5. View Question papers")
        print("q. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            response = change_password(username)
        elif choice == "2":
            response = create_question_papers(username)
            if response == True:
                print("Question papers created successfully!")
            else:
                choice = input("Try again?(y/n)").lower()
                if choice == "n":
                    break
        elif choice == "3":
            response = add_questions_to_exam_papers(username)
            if response == True:
                print("Questions added to question papers!")
            else:
                choice = input("Try again?(y/n)").lower()
                if choice == "n":
                    break
        elif choice == "4":
            response = edit_question_papers(username)
            if response == True:
                print("Questions displayed Successfully!")
            else:
                choice = input("Try again?(y/n)").lower()
                if choice == "n":
                    break
        elif choice == "5":
            response = view_question_papers(username)
            if response == True:
                print("Questions deleted Successfully!")
            else:
                choice = input("Try again?(y/n)").lower()
                if choice == "n":
                    break
        elif choice == "q":
            print("... Exiting ...")
            os.system("sleep 3")
            os.system("clear")
            exit()
        else:
            print(f"Option {choice} not available, Try again!")
