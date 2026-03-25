message = "Welcome to python programming"
print(len(message))
print(message[0:10])
print(message[:10])#start from zero
print(message[5:])# start from the defind index to the end
print(message[:])# creates a copy of the string

number = '0725439354'
print(number[0::2])
print(number[::-1])
# message[1] = 'i'

language  = 'Pithon'
corrected = language[0] + 'y' + language[2:]
print(corrected)
