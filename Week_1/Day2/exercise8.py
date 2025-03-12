def star_wars_quiz():
    data = [
        {"question": "What is Baby Yoda's real name?", "answer": "Grogu"},
        {"question": "Where did Obi-Wan take Luke after his birth?", "answer": "Tatooine"},
        {"question": "What year did the first Star Wars movie come out?", "answer": "1977"},
        {"question": "Who built C-3PO?", "answer": "Anakin Skywalker"},
        {"question": "Anakin Skywalker grew up to be who?", "answer": "Darth Vader"},
        {"question": "What species is Chewbacca?", "answer": "Wookiee"}
    ]
    correct, incorrect = 0, 0
    wrong_answers = []

    for q in data:
        user_answer = input(q["question"] + " ").strip()
        if user_answer.lower() == q["answer"].lower():
            correct += 1
        else:
            incorrect += 1
            wrong_answers.append((q["question"], user_answer, q["answer"]))

    print(f"Correct: {correct}, Incorrect: {incorrect}")
    if incorrect > 0:
        print("Here are the questions you got wrong:")
        for q, ua, ca in wrong_answers:
            print(f"Q: {q}\nYour answer: {ua}\nCorrect answer: {ca}")
    if incorrect > 3:
        print("Try again!")
star_wars_quiz()