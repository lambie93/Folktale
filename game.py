import random

print("☕🍂 Welcome to Gilmore Girls trivia! 🍂☕")
print("Think you know everything about Stars Hollow? Let's find out!")

input("\nPress Enter to start...")

questions = [
    {
        "question": "What is the name of Lorelai's inn?",
        "options": [
            "A. Dragonfly Inn",
            "B. Independence Inn",
            "C. Stars Inn",
            "D. Gilmore Inn"
        ],
        "answer": "A"
    },

    {
        "question": "What is the name of Rory's best friend?",
        "options": [
            "A. Louise",
            "B. Lane",
            "C. Madeline",
            "D. Lucy"
        ],
        "answer": "B"
    },

    {
        "question": "What university does Rory attend?",
        "options": [
            "A. Harvard",
            "B. Yale",
            "C. Princeton",
            "D. Columbia"
        ],
        "answer": "B"
    }
]

random.shuffle(questions)

score = 0

for question in questions:
    print("\n" + question["question"])

    for option in question["options"]:
        print(option)

    answer = input("\nAnswer (A, B, C, or D): ").upper().strip()

    if answer == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")
        print(f"Answer: {question['answer']}")

    input("\nPress Enter to continue...")

print(f"\n{score} out of {len(questions)}")

print("Thanks for playing!")

