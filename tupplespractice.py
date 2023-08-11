thistupple = ('apple', 'banana', 'cherry')
print(thistupple)


# Creating tupples with one element

var1 = ('Hello')
print(type(var1), var1)

var2 = ('Hello',)
print(type(var2), var2)

var3 = 'hello',
print(type(var3), var3)

fruits = 'mango', 'ornage', 'pawpaw',
print(type(fruits), fruits)


# Access Python Tuple Elements

letters = ('p', 'r', 'o', 'g', 'r', 'a', 'm')
print(letters[0])

# Negative Indexing
print(letters[-1])
print(letters[-3])


# Slicing
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
print(my_tuple[2:6]) #Printing from the 3rd position to the 6th position

# element begining to second
print(my_tuple[:-7])

# element 8th to end
print(my_tuple[7:])

# Python Tuple Method

my_fruit = ('a', 'p', 'p', 'l', 'e',)

print(my_fruit.count('p')) #prints 2
print(my_fruit.index('l')) #prints 3


# iterating through a tuple
languages = ('python', 'swift', 'c++',)
for language in languages:
    print(language)



# Checking if an item exist

print('C' in languages)
print('Python' in languages) # prints false
print('python' in languages) # prints true

