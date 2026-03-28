my_tuple = ('Esther','Nancy','Belvah','Grace')
new_tuple = tuple(my_tuple)
print(new_tuple)

print((2,7,9)<(4,6,8))

txt = 'but soft what light through yonder window breaks'
strings = txt.split()

my_words = list()
for word in strings:
    my_words.append((len(word),word))

my_words.sort(reverse=True)
new_words = list()
for length ,word in my_words:
    new_words.append(word)
print(new_words)
