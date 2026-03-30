alphabets = dict() # a constructor
alphabets['a']='apple'
alphabets['b']='ball'
alphabets['c']='cat'
my_dict = {'a':'apple','b':'ball','c':'cat'}
print(alphabets)
print(my_dict)
print(alphabets['a'])
print(len(alphabets))
print('c' in alphabets)
print('cat' in alphabets)# does not loop the values
print(alphabets.keys())
print(alphabets.values())

fname = input ('Enter a file name')
fhand = open(fname)

count = dict()
for line in fhand :
    words = line.split()
    for word in words:
       count[word] = count.get(word,0) + 1

print(count)

import string

fname = input ('Enter a file name \n')

try:
    fname =  open(fname)
except:
    print('Enter a valid file name',fname)
    exit()

count = dict()
for line in fhand :
    words = line.rstrip()
    table = str.maketrans('','',string.punctuation)
    words = line.translate(table)
    words = words.lower()
    words = line.split()
    for word in words:
        count[word] = count.get(word,0) + 1

print(count)
