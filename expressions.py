# name = input("Enter your name:\n") # A place holder for user experience
# print(name)
# age = input("Enter yor age: \n")
# print(age)

#implicit type conversion
int_num = 25
float_num = 12.75
sum = int_num + float_num
print("Value:", sum)

#explicit type conversion - type casting
num = "25"
print (type(num))
num1 = 120
num = int(num)
print (type(num))
sum = num + num1
print(sum)
  
num = 74
num1 = "72"
num1 = int(num1)
sum = num + num1
print(sum)

num = 45
num2 = "12.75"
num2 = float(num2)
print(type(num2))
num2 = int(num2)
print(type(num2))
sum = num + num2
print(sum)
