#EXCERSIZE 1
# a
print(5 / 3) # displays 1.6666666666666667 because as of python 3 the '/' operator does floating point division for ints and floats.

# b
print (5 % 3) # displays 2 because % is the modulus operator and the modulus is meant to show the remainder.

# c
print(5.0/3) # displays 1.6666666666666667 because as of python 3 the '/' operator does floating point division for ints and floats.

# d
print(5/3.0) # displays 1.6666666666666667 because as of python 3 the '/' operator does floating point division for ints and floats.

# e
print(5.2%3) # displays 2.2 because that's the remainder of 5.2 divided by 3.


#EXCERSIZE 2
# a 
#print(2000.3 ** 200) # this results in an overflow error. Because it's not a repeating number it can't be explain by simply rounding up the last number.

# b
print(1.0 + 1.0 - 1.0) # this prints 1.0 because each number in the equation is a float.

# c
print(1.0 + 1.0e20 - 1.0e20) # prints 0.0 because it's rounding as best it can. since it can't do math properly past e15.


#EXCERSIZE 3
#a
print(float(123)) # it prints 123.0 because you're casting an int to a float

#b
print(float('123')) # It prints 123.0 because you're casting a string of '123' to a float

#c
print(float('123.23')) # It prints 123.23 because you're casting a string of '123.23' to a float

#d
print(int(123.23)) # It prints 123 because you're casting a float of 123.23 into an in so it rounds down to 123

#e
#print(int('123.23')) # gives a value error saying invalid literal

# f
print(int(float('123.23'))) # this is the fix to the above conversion error

#g
print(str(12)) # prints 12

#h
print(str(12.2)) # prints 12.2

#i
print(bool('a')) # prints True because in python non-empty strings evaluate as true

#j
print(bool(0)) # prints False because a 0 is false

#k
print(bool(0.1)) # prints True because a non-zero is true

#EXCERSIZE 4

#range(5) returns range(0,5). for i in range(5) would mean for some int i in 0 or 5.
#typing type(range(5)) tells us the type 'range' is a class

#EXCERSIZE 5

numberFound = 0

x = 11
while numberFound < 20:
    if x % 5 == 0:
        if x % 7 == 0:
            if x % 11 == 0:
                print(x)
                numberFound += 1
    x += 1
    

