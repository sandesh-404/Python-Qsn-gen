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
    # Define file paths
    topics_file = "texts/topics.txt"
    questions_file = "texts/questions.txt"
    set_a_file = f"sets/set_a.txt"
    set_b_file = f"sets/set_b.txt"

    # Read topics from file
    topics = {}
    with open(topics_file, "r") as f:
        for line in f:
            topic, subject = line.strip().split("@")
            topics[subject] = topics.get(subject, [])
            topics[subject].append(topic)

    # Read questions from file
    questions = {}
    with open(questions_file, "r") as f:
        for line in f:
            parts = line.strip().split(", ")
            topic_subject = parts[0]
            section = parts[1]
            question = parts[2]
            if section == "Section_A":
                answer = parts[3]
                options = parts[4:]
                questions[topic_subject] = questions.get(topic_subject, {})
                questions[topic_subject][section] = questions[topic_subject].get(
                    section, []
                )
                questions[topic_subject][section].append((question, answer, options))
            else:
                questions[topic_subject] = questions.get(topic_subject, {})
                questions[topic_subject][section] = questions[topic_subject].get(
                    section, []
                )
                questions[topic_subject][section].append((question,))

    # Display subjects for user to choose
    print("Choose a subject:")
    for i, subject in enumerate(topics.keys()):
        print(f"{i+1}. {subject}")
    subject_choice = int(input("Enter subject number: "))
    subject = list(topics.keys())[subject_choice - 1]

    # Display topics for user to choose
    print("Choose a topic:")
    for i, topic in enumerate(topics[subject]):
        print(f"{i+1}. {topic}")
    topic_choice = int(input("Enter topic number: "))
    topic = topics[subject][topic_choice - 1]
    topic_subject = f"{topic}@{subject}"

    # Get user input for set choice
    set_choice = input("Enter set choice (A/B): ")

    # Initialize set files
    if set_choice.lower() == "a":
        set_file = set_a_file
    elif set_choice.lower() == "b":
        set_file = set_b_file
    else:
        print("Invalid set choice. Please enter A or B.")
        return False

    # Display Section A questions for user to choose
    if "Section_A" in questions[topic_subject]:
        print("Choose Section A questions:")
        for i, question in enumerate(questions[topic_subject]["Section_A"]):
            print(f"{i+1}. {question[0]} (Answer: {question[1]})")
            for j, option in enumerate(question[2]):
                print(f"  {j+1}. {option}")
        section_a_questions = []
        while len(section_a_questions) < 5:
            question_choice = input("Enter question number (or 'done' to finish): ")
            if question_choice.lower() == "done":
                break
            try:
                question_choice = int(question_choice)
                for i, question in enumerate(questions[topic_subject]["Section_A"]):
                    if i + 1 == question_choice:
                        section_a_questions.append(
                            (topic_subject, "Section_A", question[0])
                        )
                        break
            except ValueError:
                print("Invalid input. Please enter a number or 'done'.")
    else:
        print("No Section A questions available for this topic.")
        section_a_questions = []

    # Display Section B questions for user to choose
    if "Section_B" in questions[topic_subject]:
        print("Choose Section B questions:")
        for i, question in enumerate(questions[topic_subject]["Section_B"]):
            print(f"{i+1}. {question[0]}")
        section_b_questions = []
        while len(section_b_questions) < 3:
            question_choice = input("Enter question number (or 'done' to finish): ")
            if question_choice.lower() == "done":
                break
            try:
                question_choice = int(question_choice)
                for i, question in enumerate(questions[topic_subject]["Section_B"]):
                    if i + 1 == question_choice:
                        section_b_questions.append(
                            (topic_subject, "Section_B", question[0])
                        )
                        break
            except ValueError:
                print("Invalid input. Please enter a number or 'done'.")
    else:
        print("No Section B questions available for this topic.")
        section_b_questions = []

    # Write chosen questions to set file
    with open(set_file, "a") as f:
        for question in section_a_questions + section_b_questions:
            f.write(f"{question[0]}, {question[1]}, {question[2]}\n")

    print("Questions added to exam paper successfully.")
    return True


def edit_question_papers(username):
    pass


def view_question_papers(username):
    pass
