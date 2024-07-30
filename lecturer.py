def add_question_answers(username):
    questions_and_answers = []
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
    print("Available subjects:")
    for i, subject in enumerate(sorted(list(subjects)), 1):
        print(f"{i}. {subject}")
    subject_index = int(input("Select a subject (enter the number): ")) - 1
    selected_subject = sorted(list(subjects))[subject_index]
    print(f"Topics for {selected_subject}:")
    for i, topic in enumerate(topics[selected_subject], 1):
        print(f"{i}. {topic}")
    topic_index = int(input("Select a topic (enter the number): ")) - 1
    selected_topic = topics[selected_subject][topic_index]
    while True:
        section = input(
            "Select a section (A for multiple choice, B for subjective): "
        ).upper()
        if section == "A":
            question = input("Enter a question: ")
            answer = input("Enter the correct answer: ")
            option1 = input("Enter option 1: ")
            option2 = input("Enter option 2: ")
            option3 = input("Enter option 3: ")
            option4 = input("Enter option 4: ")
            questions_and_answers.append(
                (
                    f"{selected_topic}@{selected_subject}, A, {question}, {answer}, {option1}, {option2}, {option3}, {option4}"
                )
            )
        elif section == "B":
            question = input("Enter a question: ")
            answer = input("Enter the answer: ")
            questions_and_answers.append(
                (f"{selected_topic}@{selected_subject}, B, {question}, {answer}")
            )
        else:
            print("Invalid section. Please try again.")
            continue
        print("Question and answer have been recorded successfully!")
        add_another = input("Do you want to add another question and answer? (y/n): ")
        if add_another.lower() == "n":
            break
    with open("texts/questions.txt", "a") as file:
        for question in questions_and_answers:
            file.write(question + "\n")
    return True


def edit_question_answers(username):
    questions_and_answers = []
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
                questions_and_answers.append(
                    (topic_subject, section, question, answer, options)
                )
            elif section == "B":
                answer = parts[3]
                questions_and_answers.append((topic_subject, section, question, answer))
    print("Available questions:")
    for i, (topic_subject, section, question, *args) in enumerate(
        questions_and_answers, 1
    ):
        print(f"{i}. {topic_subject} - {question}")
    question_index = int(input("Select a question to edit (enter the number): ")) - 1
    topic_subject, section, question, *args = questions_and_answers[question_index]
    if section == "A":
        answer, options = args
        print(f"Current question: {question}")
        print(f"Current answer: {answer}")
        print("Current options:")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        new_question = input("Enter a new question (or press enter to keep the same): ")
        if new_question:
            question = new_question
        new_answer = input("Enter a new answer (or press enter to keep the same): ")
        if new_answer:
            answer = new_answer
        for i in range(4):
            new_option = input(
                f"Enter a new option {i+1} (or press enter to keep the same): "
            )
            if new_option:
                options[i] = new_option
        questions_and_answers[question_index] = (
            topic_subject,
            section,
            question,
            answer,
            options,
        )
    elif section == "B":
        answer = args[0]
        print(f"Current question: {question}")
        print(f"Current answer: {answer}")
        new_question = input("Enter a new question (or press enter to keep the same): ")
        if new_question:
            question = new_question
        new_answer = input("Enter a new answer (or press enter to keep the same): ")
        if new_answer:
            answer = new_answer
        questions_and_answers[question_index] = (
            topic_subject,
            section,
            question,
            answer,
        )
    with open("texts/questions.txt", "w") as file:
        for topic_subject, section, question, *args in questions_and_answers:
            if section == "A":
                answer, options = args
                file.write(
                    f"{topic_subject}, {section}, {question}, {answer}, {', '.join(options)}\n"
                )
            elif section == "B":
                answer = args[0]
                file.write(f"{topic_subject}, {section}, {question}, {answer}\n")
    print("Questions and answers recorded successfully!")
    return True


def view_question_answers(username):
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
                    questions_and_answers[topic_subject] = [
                        (section, question, answer, options)
                    ]
                else:
                    questions_and_answers[topic_subject].append(
                        (section, question, answer, options)
                    )
            elif section == "B":
                answer = parts[3]
                if topic_subject not in questions_and_answers:
                    questions_and_answers[topic_subject] = [(section, question, answer)]
                else:
                    questions_and_answers[topic_subject].append(
                        (section, question, answer)
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
        subject_index = input("Select a subject (enter the number), or 'q' to quit: ")
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
            for i, (section, question, *args) in enumerate(
                questions_and_answers[selected_topic + "@" + selected_subject], 1
            ):
                if section == "A":
                    answer, options = args
                    print(f"{i}. {question} - {answer} (Options: {', '.join(options)})")
                elif section == "B":
                    answer = args[0]
                    print(f"{i}. {question} - {answer}")
        else:
            print(f"No questions for {selected_topic}")


def delete_question_answers(username):
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
                    questions_and_answers[topic_subject] = [
                        (section, question, answer, options)
                    ]
                else:
                    questions_and_answers[topic_subject].append(
                        (section, question, answer, options)
                    )
            elif section == "B":
                answer = parts[3]
                if topic_subject not in questions_and_answers:
                    questions_and_answers[topic_subject] = [(section, question, answer)]
                else:
                    questions_and_answers[topic_subject].append(
                        (section, question, answer)
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
        subject_index = input("Select a subject (enter the number), or 'q' to quit: ")
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
            for i, (section, question, *args) in enumerate(
                questions_and_answers[selected_topic + "@" + selected_subject], 1
            ):
                if section == "A":
                    answer, options = args
                    print(f"{i}. {question} - {answer} (Options: {', '.join(options)})")
                elif section == "B":
                    answer = args[0]
                    print(f"{i}. {question} - {answer}")
            while True:
                delete_index = input(
                    "Select a question to delete (enter the number), or 'q' to quit: "
                )
                if delete_index.lower() == "q":
                    break
                try:
                    delete_index = int(delete_index) - 1
                    section_to_delete, question_to_delete, *args_to_delete = (
                        questions_and_answers[
                            selected_topic + "@" + selected_subject
                        ].pop(delete_index)
                    )
                    if section_to_delete == "A":
                        answer_to_delete, options_to_delete = args_to_delete
                        print(
                            f"Deleted question: {question_to_delete} - {answer_to_delete} (Options: {', '.join(options_to_delete)})"
                        )
                    elif section_to_delete == "B":
                        answer_to_delete = args_to_delete[0]
                        print(
                            f"Deleted question: {question_to_delete} - {answer_to_delete}"
                        )
                except (ValueError, IndexError):
                    print("Invalid question index. Please try again.")
                    continue
            with open("texts/questions.txt", "w") as file:
                for topic, questions in questions_and_answers.items():
                    for section, question, *args in questions:
                        if section == "A":
                            answer, options = args
                            file.write(
                                f"{topic}, {section}, {question}, {answer}, {', '.join(options)}\n"
                            )
                        elif section == "B":
                            answer = args[0]
                            file.write(f"{topic}, {section}, {question}, {answer}\n")
            print("Questions updated successfully.")
        else:
            print(f"No questions for {selected_topic}")
