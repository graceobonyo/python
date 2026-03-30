students_ids = {201,202,203,204}
my_set = {1,"Joseph",2.5 ,()}
print(type(my_set))

my_students = {}
print(type(my_students))

my_hash = {2,'Nancy',3.8,('Grace','Esther',909)}
print(my_hash)

my_students = set()
print(type(my_students))

#CRUD
my_hash.add('Belvah')
print(my_hash)
my_hash.update(['Belvah','Cynthia'])
print(my_hash)

popped = my_hash.pop()
print(popped)

#union
a = {1,2,}
b = {1,2,3,4,5}
print(a | b)
print(a.union(b))
print (a&b)
print(b-b)
print(b-a)
print(a ^ b)
print(a.issubset(b))
print(a.issubset(a))
print (b.isdisjoint(a))

