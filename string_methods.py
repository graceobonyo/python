my_string = "Python Programming"
print(len(my_string))
my_string.lower()
print(my_string.lower())
print(my_string.upper())
print(my_string.capitalize())
print(my_string.title())
print(my_string.swapcase())

city = "mississipi"
#searching for a given substring from the string
print(my_string.find('gi')) # returns the index of the substring from thr string
print(my_string.count('o'))
print(city.count('iss'))

clean = my_string.strip()
cleaned = my_string.lstrip()
cleaned = my_string.rstrip
print(clean)

# Validation
file = 'my _work.txt'
if file.endswith('.pdf'):
    print("The file is valid")
else:
    print("Invalid file format")

age = "22"
if age.isdigit():
    # age = int(age)
    print(age)

message = "I love programming. Python is the way to go in 2026 "
new_message = message.replace('love','hate')
print(new_message)
my_message = message.split(".")
print(my_message)

fruits = "pineapple,peach,guava"
my_fruits = fruits.split(',')
print(my_fruits)

language = ['J','a','v','a','s','c','r','i','p','t']
print(''.join(language))

email = "USER_Name@UT.AC.UK \n"
clean_email = email.strip().lower().replace('_','.')
print(clean_email)
