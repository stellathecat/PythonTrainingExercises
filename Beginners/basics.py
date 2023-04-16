# Given
x = 10000.0
y = 3.0
print(x / y)
print(10000 / 3)
# What is happening?

# Given
print(x - 1 / y)
print((x - 1) / y)
# What is happening?

# Given 
x = 'foo'
y = 'bar'
# Create 'foobar' using x and y
x+y
# Create 'foo -> bar' using x and y
x+' -> '+y
f"{x} -> {y}"

# Given
x = 'hello world'
# from x create 'HELLO WORLD'
x.upper()
# from x create 'hellX wXrld'
x.replace('o', 'X')

# Given
x = 10000.0
y = 3.0
# print "10000 / 3 = 3333" using x and y
from math import floor
floor(z)
x//y

# Given
x = ['hello', 'world']
# print 'helloworld'
# print 'hello world'
# print 'hello
# world'
print(x[0], '\n', x[1])

# Given
x = "Monty Python and the Holy Grail"
# create the list ['Monty', 'Python', 'and', 'the', 'Holy', 'Grail']
x.split()
y = "one,two,three,four"
# create the list ['one', 'two', 'three', 'four'
y.split(sep = ",")