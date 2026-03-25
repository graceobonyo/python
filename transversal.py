word = 'banana'
index = 0

while index < len(word):
    char = word [index]
    print(f'Index{index} contains:{char}')
    index += 1

for char in word :
    if char == 'n':
        index = index +1
        print(index)
#for char in word:
#    print(char)  
print('ban' in word)# return boolean

email = 'graceobonyo@gmail.com'
print('@gmail' in email) 

fruit = 'Pineapple'
if word < 'Pineapple':
    print('banana comes first')