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
        question = input("Enter a question: ")
        answer = input("Enter an answer: ")
        questions_and_answers.append(
            (f"{selected_topic}@{selected_subject}", question, answer)
        )
        print("Question and answer have been recorded successfully!")
        add_another = input("Do you want to add another question and answer? (y/n): ")
        if add_another.lower() == "n":
            break
    with open("texts/questions.txt", "a") as file:
        for topic, question, answer in questions_and_answers:
            file.write(f"{topic}, {question}, {answer}\n")
    return True


def edit_question_answers(username):
    # The same as the above to add the questions but in this function we are going to edit the questions and answers but not subject and topic
    questions_and_answers = []
    with open("texts/questions.txt", "r") as file:
        for line in file:
            topic, question, answer = line.strip().split(", ")
            questions_and_answers.append((topic, question, answer))
    print("Available questions:")
    for i, (topic, question, answer) in enumerate(questions_and_answers, 1):
        print(f"{i}. {topic} - {question}")
    question_index = int(input("Select a question to edit (enter the number): ")) - 1
    topic, question, answer = questions_and_answers[question_index]
    print(f"Current question: {question}")
    print(f"Current answer: {answer}")
    new_question = input("Enter a new question (or press enter to keep the same): ")
    if new_question:
        question = new_question
    new_answer = input("Enter a new answer (or press enter to keep the same): ")
    if new_answer:
        answer = new_answer
    questions_and_answers[question_index] = (topic, question, answer)
    with open("texts/questions.txt", "w") as file:
        for topic, question, answer in questions_and_answers:
            file.write(f"{topic}, {question}, {answer}\n")
            print("Questions and answers recorded successfully!")
    return True


def view_question_answers(username):
    questions_and_answers = {}
    with open("texts/questions.txt", "r") as file:
        for line in file:
            topic, question, answer = line.strip().split(", ")
            topic, subject = topic.strip().split("@")
            if topic not in questions_and_answers:
                questions_and_answers[topic] = [(question, answer)]
            else:
                questions_and_answers[topic].append((question, answer))
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
        if selected_topic in questions_and_answers:
            print(f"Questions for {selected_topic}:")
            for i, (question, answer) in enumerate(
                questions_and_answers[selected_topic], 1
            ):
                print(f"{i}. {question} - {answer}")
        else:
            print(f"No questions for {selected_topic}")


def delete_question_answers(username):
    questions_and_answers = {}
    with open("texts/questions.txt", "r") as file:
        for line in file:
            topic, question, answer = line.strip().split(", ")
            topic, subject = topic.strip().split("@")
            if topic not in questions_and_answers:
                questions_and_answers[topic] = [(question, answer)]
            else:
                questions_and_answers[topic].append((question, answer))
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
        if selected_topic in questions_and_answers:
            print(f"Questions for {selected_topic}:")
            for i, (question, answer) in enumerate(
                questions_and_answers[selected_topic], 1
            ):
                print(f"{i}. {question} - {answer}")
            while True:
                delete_index = input(
                    "Select a question to delete (enter the number), or 'q' to quit: "
                )
                if delete_index.lower() == "q":
                    break
                try:
                    delete_index = int(delete_index) - 1
                    question_to_delete, answer_to_delete = questions_and_answers[
                        selected_topic
                    ].pop(delete_index)
                    print(
                        f"Deleted question: {question_to_delete} - {answer_to_delete}"
                    )
                except (ValueError, IndexError):
                    print("Invalid question index. Please try again.")
                    continue
            with open("texts/questions.txt", "w") as file:
                for topic, questions in questions_and_answers.items():
                    for question, answer in questions:
                        file.write(f"{topic}@{question}, {answer}\n")
            print("Questions updated successfully.")
        else:
            print(f"No questions for {selected_topic}")
