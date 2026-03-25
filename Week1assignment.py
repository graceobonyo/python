
# QUIZ GAME

def welcome_to(game):
    print(f"Welcome to {game}!")
welcome_to("Know Your Country")

def choose(instructions):
    print(f"Choose {instructions}!")
choose("one correct answer only")


questions = [
    {
        "question": "When did Kenya gain independence?",
        "choices": {"A": "1895", "B": "1920", "C": "1963", "D": "1964"},
        "answer": "C"
    },
    {
        "question": "How many prime ministers has Kenya had?",
        "choices": {"A": "8", "B": "9", "C": "3", "D": "2"},
        "answer": "D"
    },
    {
        "question": "What sport is Kenya worldwide known for?",
        "choices": {"A": "Athletics", "B": "Cricket", "C": "Ice Hockey", "D": "Ballet"},
        "answer": "A"
    },
    {
        "question": "Kenya has how many counties?",
        "choices": {"A": "47", "B": "83", "C": "64", "D": "39"},
        "answer": "A"
    },
]


score = 0  #  score starts at 0
total = len(questions)

for q in questions:
    print("\n" + q["question"])
    for option, text in q["choices"].items():
        print(f"  {option}. {text}")

    while True:
        user_answer = input("Your answer: ").strip().upper()
        if user_answer in ["A", "B", "C", "D"]:
            break
        else:
            print("Invalid input. Please enter A, B, C, or D.")

    if user_answer == q["answer"]:
        print(" Correct!\n")
        score += 1       #  Add score properly
    else:
        print(f"Wrong! The correct answer was {q['answer']}.\n")

print("QUIZ COMPLETE!")
print(f"Your final score: {score} / {total}")

if score == total:
    print("Excellent! Perfect score!")
elif score >= total * 0.6:
    print("Good")
