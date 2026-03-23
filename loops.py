def sum_numbers(*args):
    return sum(args)
print(sum_numbers(12,34))

def show_profile(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
show_profile(name="Grace",age=22,city="Nairobi") 


word = "banana"

for var in word:
    print(var)

friends = ['Grace','Belvah','Nancy','Cynthia']
for friend in friends:
    print(f'Hello!{friend}')


Weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday']
for Weekday in Weekdays:
    print(f'Good morning this!{Weekday}')
    
Numbers = [0,10,20,30,40,50,60]
for Number in Numbers:
    print(Number)

scores = [96,88,70,65,72,99,55]
for score in scores:
    if score >= 90:
     print(f'Found the highest scorer with {score}')

# while loop
# initialisation step
num = 1000
while num > 0:
    if num == 800:
        break 
    print(num)
    # increment step
    num = num - 1
print('Finished looping')

Word = 'Python'

while True:
    guess = str(input("Which is the most popular programming language in 2026?...\n"))
    if guess == '':
        print('Please enter a valid guess')
        continue
    if guess == Word :
        print('Congratulations,you guesssed it right!')
        break
    print('Nice attempt please try again another time')

Number = 3
while True:
    answer = int(input("What is 27 divided by 9?...\n"))
    if answer == '':
        print('Please enter a number')
        continue
    if answer == Number :
        print('Good job!Procceed to the next level')
        break
    print('Good one buddy please try again')

my_num = 7
while True:
    guess = int(input('Give me an prime number between 1 and 10')) #1
    if guess < 0:
        print("Enter a positive number")
        continue
    if guess == my_num:
        print('Congratulations you made it')
        break
    print('Please try again...')
    