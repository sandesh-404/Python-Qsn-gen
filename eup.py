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

    # Get user input for set choice
    print("Choose a set:")
    print("1. Set A")
    print("2. Set B")
    set_choice = input("Enter set number: ")
    if set_choice == "1":
        set_file = set_a_file
    elif set_choice == "2":
        set_file = set_b_file
    else:
        print("Invalid set choice. Please enter 1 or 2.")
        return False

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

    # Display Section A questions for user to choose
    if "Section_A" in questions[topic_subject]:
        print("Choose Section A questions:")
        for i, question in enumerate(questions[topic_subject]["Section_A"]):
            print(f"{i+1}. {question[0]}")
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
                            (
                                topic_subject,
                                "Section_A",
                                question[0],
                                question[2],
                            )
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
    with open(set_file, "w") as f:
        for question in section_a_questions:
            f.write(
                f"{question[0]}, {question[1]}, {question[2]}, {', '.join(question[3])}\n"
            )
        for question in section_b_questions:
            f.write(f"{question[0]}, {question[1]}, {question[2]}\n")

    print("Questions added to exam paper successfully.")
    return True


def edit_question_papers(username):
    # Define file paths
    questions_file = "texts/questions.txt"
    set_a_file = "sets/set_a.txt"
    set_b_file = "sets/set_b.txt"

    # Read questions from file
    questions = {}
    with open(questions_file, "r") as f:
        for line in f:
            parts = line.strip().split(", ")
            if len(parts) < 3:
                print(f"Skipping line: {line} (not enough values)")
                continue
            topic_subject = parts[0]
            section = parts[1]
            if len(parts) > 2:
                question = parts[2]
            else:
                question = ""
            if section == "Section_A":
                if len(parts) > 3:
                    answer = parts[3]
                else:
                    answer = ""
                if len(parts) > 4:
                    options = parts[4:]
                else:
                    options = []
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

    # Get user input for set choice
    print("Choose a set:")
    print("1. Set A")
    print("2. Set B")
    set_choice = input("Enter set number: ")
    if set_choice == "1":
        set_file = set_a_file
    elif set_choice == "2":
        set_file = set_b_file
    else:
        print("Invalid set choice. Please enter 1 or 2.")
        return False

    # Read existing questions from set file
    existing_questions = {}
    with open(set_file, "r") as f:
        for line in f:
            parts = line.strip().split(", ")
            if len(parts) < 3:
                print(f"Skipping line: {line} (not enough values)")
                continue
            topic_subject = parts[0]
            section = parts[1]
            if len(parts) > 2:
                question = parts[2]
            else:
                question = ""
            existing_questions[topic_subject] = existing_questions.get(
                topic_subject, {}
            )
            existing_questions[topic_subject][section] = existing_questions[
                topic_subject
            ].get(section, [])
            if section == "Section_A":
                if len(parts) > 3:
                    options = parts[3:]
                else:
                    options = []
                existing_questions[topic_subject][section].append((question, options))
            else:
                existing_questions[topic_subject][section].append((question,))

    # Replace Section A questions
    print("Replace Section A questions:")
    topic_subject = "physics@science"
    section = "Section_A"
    if (
        topic_subject in existing_questions
        and section in existing_questions[topic_subject]
    ):
        for i, question in enumerate(existing_questions[topic_subject][section]):
            print(f"{i+1}. {question[0]}")
        section_a_questions_to_replace = input(
            "Enter question numbers to replace (comma-separated): "
        ).split(", ")
        for question_number in section_a_questions_to_replace:
            question_number = int(question_number)
            if question_number > 0 and question_number <= len(
                existing_questions[topic_subject][section]
            ):
                question = existing_questions[topic_subject][section][
                    question_number - 1
                ][0]
                print("Choose a new question:")
                for i, new_question in enumerate(questions[topic_subject][section]):
                    print(f"{i+1}. {new_question[0]} (Answer: {new_question[1]})")
                    for j, option in enumerate(new_question[2]):
                        print(f"  {j+1}. {option}")
                new_question_choice = int(input("Enter new question number: "))
                new_question = questions[topic_subject][section][
                    new_question_choice - 1
                ]
                existing_questions[topic_subject][section][question_number - 1] = (
                    new_question[0],
                    new_question[2],
                )
            else:
                print(f"Invalid question number: {question_number}")
    else:
        print("No questions found in Section A")

    # Replace Section B questions
    print("Replace Section B questions:")
    topic_subject = "physics@science"
    section = "Section_B"
    if (
        topic_subject in existing_questions
        and section in existing_questions[topic_subject]
    ):
        for i, question in enumerate(existing_questions[topic_subject][section]):
            print(f"{i+1}. {question[0]}")
        section_b_questions_to_replace = input(
            "Enter question numbers to replace (comma-separated): "
        ).split(", ")
        for question_number in section_b_questions_to_replace:
            question_number = int(question_number)
            if question_number > 0 and question_number <= len(
                existing_questions[topic_subject][section]
            ):
                question = existing_questions[topic_subject][section][
                    question_number - 1
                ][0]
                print("Choose a new question:")
                for i, new_question in enumerate(questions[topic_subject][section]):
                    print(f"{i+1}. {new_question[0]}")
                new_question_choice = int(input("Enter new question number: "))
                new_question = questions[topic_subject][section][
                    new_question_choice - 1
                ]
                existing_questions[topic_subject][section][question_number - 1] = (
                    new_question[0],
                )
            else:
                print(f"Invalid question number: {question_number}")
    else:
        print("No questions found in Section B")

    # Write replaced questions back to set file
    with open(set_file, "w") as f:
        for topic_subject, sections in existing_questions.items():
            for section, questions in sections.items():
                for question in questions:
                    if section == "Section_A":
                        f.write(
                            f"{topic_subject}, {section}, {question[0]}, {', '.join(question[1])}\n"
                        )
                    else:
                        f.write(f"{topic_subject}, {section}, {question[0]}\n")
    print("Questions edited successfully.")
    return True


def view_question_papers(username):
    # Get list of available sets
    import os

    sets_dir = "sets/"
    sets = [
        f for f in os.listdir(sets_dir) if f.startswith("set") and f.endswith(".txt")
    ]

    # Display available sets and ask user to choose one
    print("Available sets:")
    for i, set_file in enumerate(sets, 1):
        print(f"{i}. {set_file}")

    while True:
        choice = input("Enter the number of the set you want to view: ")
        if choice.isdigit() and 1 <= int(choice) <= len(sets):
            set_file = sets[int(choice) - 1]
            break
        else:
            print("Invalid choice. Please try again.")

    # Read existing questions from set file
    existing_questions = {}
    set_file_path = os.path.join(
        sets_dir, set_file
    )  # Join the directory path with the file name
    with open(set_file_path, "r") as f:
        for line in f:
            parts = line.strip().split(", ")
            if len(parts) < 3:
                print(f"Skipping line: {line} (not enough values)")
                continue
            topic_subject = parts[0]
            section = parts[1]
            if len(parts) > 2:
                question = parts[2]
            else:
                question = ""
            if section == "Section_A":
                if len(parts) > 3:
                    options = parts[3:]
                else:
                    options = []
                existing_questions[topic_subject] = existing_questions.get(
                    topic_subject, {}
                )
                existing_questions[topic_subject][section] = existing_questions[
                    topic_subject
                ].get(section, [])
                existing_questions[topic_subject][section].append((question, options))
            else:
                existing_questions[topic_subject] = existing_questions.get(
                    topic_subject, {}
                )
                existing_questions[topic_subject][section] = existing_questions[
                    topic_subject
                ].get(section, [])
                existing_questions[topic_subject][section].append((question,))

    # Display question paper
    print("\nQuestion Paper")
    print(f"Set {set_file.split('.')[0]}")

    for topic_subject, sections in existing_questions.items():
        for section, questions in sections.items():
            if section == "Section_A":
                print(f"{section}:")
                for i, (question, options) in enumerate(questions, 1):
                    print(f"Q{i}. {question}")
                    # Display options
                    for j, option in enumerate(options, 97):
                        print(f"{chr(j)}. {option}")
            elif section == "Section_B":
                print(f"\n{section}:")
                for i, (question,) in enumerate(questions, 6):
                    print(f"Q{i}. {question}")