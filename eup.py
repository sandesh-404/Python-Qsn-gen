import os


def create_question_papers(username):
    choice = input("Do you want to create new question paper(y/n)?").lower()
    if choice == "y":
        question_set = input("Set A(a) or Set B(b)?(a/b/q)").lower()
        if question_set == "a":
            file_name = f"set_{question_set}.txt"
        elif question_set == "b":
            file_name = f"set_{question_set}.txt"
        elif question_set == "q":
            print("Exiting...")
            return False
        else:
            print("Invalid choice. Please try again.")
            return False

        if os.path.exists(file_name):
            override = input(
                f"{file_name} already exists. Do you want to override it? (yes/no): "
            )
            if override.lower() != "yes":
                print("Question paper not created.")
                return True

        with open(f"sets/{file_name}", "w") as f:
            f.write(f"{file_name}")

        print(f"{file_name} created successfully.")
    else:
        print("Exiting...")


def add_questions_to_exam_papers(username):
    choice = input("Do you want to add questions to existing exam paper(y/n)?").lower()
    if choice == "y":
        file_name = input("Choose set (a/b):")
        if file_name not in ["a", "b"]:
            print("Invalid set. Please choose 'a' or 'b'.")
            return False
        questions_and_answers = {}
        with open("texts/questions.txt", "r") as file:
            for line in file:
                line = line.strip()
                parts = line.split(", ")
                topic_subject = parts[0]
                section = parts[1]
                question = parts[2]
                if section == "A":
                    answer = parts[3]
                    options = parts[4:]
                    if topic_subject not in questions_and_answers:
                        questions_and_answers[topic_subject] = {
                            "A": [(question, answer, options)],
                            "B": [],
                        }
                    else:
                        questions_and_answers[topic_subject]["A"].append(
                            (question, answer, options)
                        )
                elif section == "B":
                    answer = parts[3]
                    if topic_subject not in questions_and_answers:
                        questions_and_answers[topic_subject] = {
                            "A": [],
                            "B": [(question, answer)],
                        }
                    else:
                        questions_and_answers[topic_subject]["B"].append(
                            (question, answer)
                        )
        print("Subjects:")
        with open("texts/topics.txt", "r") as file:
            subjects = set()
            topics = {}
            for line in file:
                topic, subject = line.strip().split("@")
                if subject not in subjects:
                    subjects.add(subject)
                    topics[subject] = [topic]
                else:
                    topics[subject].append(topic)
        while True:
            print("Available subjects:")
            for i, subject in enumerate(sorted(list(subjects)), 1):
                print(f"{i}. {subject}")
            subject_index = input(
                "Select a subject (enter the number), or 'q' to quit: "
            )
            if subject_index.lower() == "q":
                break
            try:
                subject_index = int(subject_index) - 1
                selected_subject = sorted(list(subjects))[subject_index]
            except (ValueError, IndexError):
                print("Invalid subject index. Please try again.")
                continue
            print(f"Topics for {selected_subject}:")
            for i, topic in enumerate(topics[selected_subject], 1):
                print(f"{i}. {topic}")
            topic_index = input("Select a topic (enter the number), or 'q' to quit: ")
            if topic_index.lower() == "q":
                break
            try:
                topic_index = int(topic_index) - 1
                selected_topic = topics[selected_subject][topic_index]
            except (ValueError, IndexError):
                print("Invalid topic index. Please try again.")
                continue
            if selected_topic + "@" + selected_subject in questions_and_answers:
                print(f"Questions for {selected_topic}:")
                section_a_questions = questions_and_answers[
                    selected_topic + "@" + selected_subject
                ]["A"]
                section_b_questions = questions_and_answers[
                    selected_topic + "@" + selected_subject
                ]["B"]
                selected_questions = []
                if len(section_a_questions) < 5:
                    print("Section A questions:")
                    for i, (question, answer, options) in enumerate(
                        section_a_questions, 1
                    ):
                        print(
                            f"{i}. {question} - {answer} (Options: {', '.join(options)})"
                        )
                    for i in range(5 - len(section_a_questions)):
                        while True:
                            question_index = input(
                                f"Select a section A question (enter the number), or 'q' to quit: "
                            )
                            if question_index.lower() == "q":
                                break
                            try:
                                question_index = int(question_index) - 1
                                selected_questions.append(
                                    section_a_questions[question_index]
                                )
                                break
                            except (ValueError, IndexError):
                                print("Invalid question index. Please try again.")
                                continue
                else:
                    print("No more section A questions can be added.")
                if len(section_b_questions) < 3:
                    print("Section B questions:")
                    for i, (question, answer) in enumerate(section_b_questions, 1):
                        print(f"{i}. {question} - {answer}")
                    for i in range(3 - len(section_b_questions)):
                        while True:
                            question_index = input(
                                f"Select a section B question (enter the number), or 'q' to quit: "
                            )
                            if question_index.lower() == "q":
                                break
                            try:
                                question_index = int(question_index) - 1
                                selected_questions.append(
                                    section_b_questions[question_index]
                                )
                                break
                            except (ValueError, IndexError):
                                print("Invalid question index. Please try again.")
                                continue
                    else:
                        print("No more section B questions can be added.")
                    print("Selected questions:")
                    for i, (question, answer, *args) in enumerate(
                        selected_questions, 1
                    ):
                        if len(args) > 0:
                            answer, options = args
                            print(
                                f"{i}. {question} - {answer} (Options: {', '.join(options)})"
                            )
                        else:
                            answer = args[0]
                            print(f"{i}. {question} - {answer}")
                    while True:
                        override = input(
                            "Do you want to override any questions(y/n)? "
                        ).lower()
                        if override == "y":
                            for i, (question, answer, *args) in enumerate(
                                selected_questions, 1
                            ):
                                if len(args) > 0:
                                    answer, options = args
                                    print(
                                        f"{i}. {question} - {answer} (Options: {', '.join(options)})"
                                    )
                                else:
                                    answer = args[0]
                                    print(f"{i}. {question} - {answer}")
                            question_index = input(
                                "Select a question to override (enter the number), or 'q' to quit: "
                            )
                            if question_index.lower() == "q":
                                break
                            try:
                                question_index = int(question_index) - 1
                                selected_questions.pop(question_index)
                                break
                            except (ValueError, IndexError):
                                print("Invalid question index. Please try again.")
                                continue
                        elif override == "n":
                            break
                        else:
                            print("Invalid input. Please enter 'y' or 'n'.")
                    with open(f"texts/set_{file_name}.txt", "a") as file:
                        for question, answer, *args in selected_questions:
                            if len(args) > 0:
                                answer, options = args
                                file.write(
                                    f"{question}, {answer}, {', '.join(options)}\n"
                                )
                            else:
                                answer = args[0]
                                file.write(f"{question}, {answer}\n")
                    print("Questions added successfully.")
                    break
                else:
                    print(f"No questions for {selected_topic}")
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


def edit_question_papers(username):
    pass


def view_question_papers(username):
    pass
