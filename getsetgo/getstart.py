# a = 1 + 2 + 3 + \
#     4 + 5 + 6 + \
#     7 + 8 + 9


a = (1 + 2 + 3 +
    4 + 5 + 6 +
    7 + 8 + 9)

# print a

colors = ['red',
          'blue',
          'green']

# print colors

for i in range(1,11):
    print i
    if i == 5:
        break

def double(num):
    """Function to double the value"""
    return 2*num
print(double.__doc__)
# Function to double the value

a, b, c = 5, 3.2, "Hello"
print (a)
print (b)
print (c)

x = y = z = "same"

print (x)
print (y)
print (z)

PI = 3.14
GRAVITY = 9.8
#
# import constant

print(PI)
print(GRAVITY)

fruits = ["apple", "mango", "orange"] #list
numbers = (1, 2, 3) #tuple
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} #dictionary
vowels = {'a', 'e', 'i' , 'o', 'u'} #set

print(fruits)
print(numbers)
print(alphabets)
print(vowels)