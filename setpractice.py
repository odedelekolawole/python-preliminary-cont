# Sets in Python

# A set is a collection of unique data. That is elements in set cannot be duplicated. Set can be used to store the IDs of students


# set of integer

student_id = {112, 112, 114, 116, 118, 115}
# print(student_id) #prints {112, 114, 116, 118, 115}

vowels = {'a', 'e', 'i', 'o', 'u'}
# print('Vowel Letters:',vowels)

# creating n empty set
# to create an empty set we use se()

empty_set = set()

# To create an empty dictionary
empty_dictionary = dict()
# print(empty_dictionary)

# Note that se can not be duplicated
numbers = {2, 4, 6, 6, 2, 8}
# print(numbers)

# Add and update set Update set in python
# Note That set are mutable

companies = {'Lacoste', 'Ralph Lauren'}

tech_companies = ['apple', 'google', 'apple']
companies.update(tech_companies)

# print(companies)

# Removing an element from a set
# the discard() methos is use to remove the specified element fom a set

langs = {'Swift', 'Java', 'Python'}
langs.discard('Python')
print(langs)


# Iterating Ove  a set in Python

sports = {'Basketball', 'Football', 'Tenis'}

for sport in sports:
    if sport == 'Basketball':
        print(f'{sport} is my favourite sport')
    elif sport == "Football":
        print(f'{sport} is my cousin\'s favourite')
    elif sport == 'Tenis':
        print(f'{sport} is my uncle\'s favourite')
    else:
        break


# Find Number in Set

even = {2, 4, 6, 8}
print(even)
print(len(even))
print(2 in even)
print(10 in even)
print(10 != even)
print(10 is not even)
print(10 in even != True)
print(10 is not even == True)
print(10 is not even != False)



# Python Set Operation
# Union of Sets
# The union of set A and B include all the elements of set A and B
# We use the | operator or the 'union()' method to perform the set union operation.

A = {1, 3, 5}
B = {0, 2, 4}
C = A|B
D = A.union(B)
print(C, D)

# Set Intersection
# The intersection of set means that the coomon element between the sets
E = {1, 3, 5}
F = {1, 2, 3}
G = E&F
H = E.intersection(F)
print(G, H)


# Different Between Two Sets
# The diffence between Set A and set B are the elements in A not in 
I = {2, 3, 5}
J = {1, 2, 6}
L = I - J
M = I.difference(B)
print(L, M)


L = J - I
N = J.difference(I)
print(L, N)


# Set Symmetric Difference
# The symmetric diffence between two sets A and B includes all the elements of A and B without the common element(s)
O = {2, 3, 5}
P = {2, 3, 1}
Q = O ^ P
R = O.symmetric_difference(P)
print(Q, R)

# Checking if two sets are equal
S = {1, 3, 5}
T = {3, 5, 1, 5}

if S == T:
    print("The sets are equal")
else:
    print("The set are not equall")