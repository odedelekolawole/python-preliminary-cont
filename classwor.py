# create a dictionary wit variable name students wuth name, age and course
# Add +a new item called gender
# Update the of the age to 5 years later
# Retrieve all the keys in the students dictionary
# Retrieve all the values in the student dictionary

# No1
students = {
    'name': "Kolawole",
    'age': 15,
    'course': 'Backend'
}

# No2
name_add = students['name2'] = 'Ayodeji'
print(name_add)
print(students)

# No3
updated_age = students['age'] = 20
print(students)

# No4
students_key = list(students.keys())
print(students_key)


# No 5
students_value = list(students.values())
print(students_value)



