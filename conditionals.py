# if the language is python give a welcome message 
language = "JavaScript"
if language == "Python":
    print("Welcome to python programming!")
else:
    print("Select your language!")

# if the marks is 92 give passed
marks = 80
if marks == 92:
    print("passed")
else :
    print("getting there")

# Short circuit evaluation
age = 11
if age > 18:
    print("You are an adult!Welcome to the club!")
elif age < 18 and age > 12:
    print("You are a teenager!You can go to class and read")
else:
    print("You are a toddler!")

