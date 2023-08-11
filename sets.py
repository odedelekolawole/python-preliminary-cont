numbers = {5, 6, 9, 6, 7, 8, 8, 2, 2, 3,}
print(set(numbers))


numbers.add(60)
print(numbers)



another = {60, 70}

numbers.update(another)
print(numbers)


fruits = {'Apple', 'Mango', 'Banana'}

new_fruits = list(fruits)

for fruit in new_fruits[0]:
    print(fruit)


    # Python Set Operation

A = {1, 3, 5}
B = {1, 2, 3}

c = A.union(B)
print(c)


d = A & B
# print(d)

e = A.intersection(B)

Difference betwen