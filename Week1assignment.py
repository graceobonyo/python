# QUIZ GAME

questions = "What is the capital city of Kenya?"
"How may prime ministers has Kenya had?"
"What is the sport Kenya is worldwide known for?"
"Kenya has how many counties?"


def welcome_to(game):
    print(f"Welcome to {game}!")
welcome_to("know your country")


answer = 'B'

while True:
    guess = str(input("What is the capital city of kenya?... A.Cairo B.Nairobi C.London D.BurkinaFaso\n"))
    if guess == '':
        print('Please enter an answer to proceed with the game')
        continue
    if guess == answer :
        print('Woohoo!Welcome to the next step')
        break
    print('Nice attempt! Please try again')


my_answer = 'D'

while True:
    guess = str(input("How many prime ministers has kenya had?.... A.8 B.9 C.3 D.2 \n"))
    if guess == '':
        print('Please enter an answer to proceed with the game')
        continue
    if guess == my_answer :
        print('Woohoo!Welcome to the next step')
        break
    print('it is okay')
        


choice = 'A'
while True:
    guess = str(input("What is the sport kenya is worldwide known for?....A.Athletics B.Cricket C.Ice Hockey D.Ballet\n"))
    if guess == '':
        print("Haiyaaa!Fill in your answer")
        continue
    if guess == choice:
        print("Good job !one more question to go")
        break
    print("You can do this!Try again")


my_choice = 'A'

while True:
    guess = str(input("Kenya has how many counties?..... A.47 B.83 C.64 D.39\n"))
    if guess == '':
        print("Please insert a valid character")
        continue
    if guess == my_choice:
        print("Congratulations!You know your country")
        break
    print("Please try again...")



