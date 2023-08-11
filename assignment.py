# Question 1
# Write a Python script to add a key to a dictionary
#         Sample Dictionary: {0: 10, 1: 10}
#         Expected Result: {0: 10, 1: 20, 2: 20}


# Question 2
# Write a Python Script to concatenate the following dictionaries to create a new one
#     Sample Dictionary
#     dict1 = {1: 10, 2: 20}
#     dict2 = {3: 30, 4: 40}
#     dict3 = {5: 50, 6: 60}
# Expected Result:
#     Result = {1: 10, 2: 20 ,3: 30, 4: 40, 5: 50, 6: 60}



# Question 3
# Write a Python Script to check whether a given key exists in a dictionary. (Use any dictionary as an example)


# Question 4
# Write a Python Script to iterate over a dictionary using loops. (Use any dictionary as an example)



# Question 5
# My_list = [34, 56, 78, 978, 45, 23, 46, 788, 24]
#     * Write a Python program to sum up all the items in a list
#     * Write a Python program to multiply all the items in a list
#     * Write a Python program to get the largest number from the list


# Write a Python script to add a key to a dictionary
print("QUESTION ONE SOLUTION")
print("----------------------------------------")
number_collection = {0: 10, 1: 10}
new_collection = number_collection[2] = 20
print(f"{new_collection} with the key '2' is added to the number_collection to give the expected ouput {number_collection}. Please try again")



# Write a Python Script to concatenate the following dictionaries to create a new one
print("QUESTION TWO SOLUTION")
print("----------------------------------------")
dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}

result = {}

result.update(dict1)
result.update(dict2)
result.update(dict3)
print(type(result), result)



# Write a Python Script to check whether a given key exists in a dictionary. (Use any dictionary as an example)
print("QUESTION THREE SOLUTION")
print("----------------------------------------")
my_dict = {
    "brand": 'Ford',
    "Model": 'Mustang',
    "Year": "1964",
    "class": "First"
}

check = input('Enter the Key you want to confirm:  ')
confirm = check in my_dict.keys()
if confirm == True:
        print(f'{check}: It exists in the dictionary')
else:
        print(f'The key you entered is not found in the ddictionary keys: {my_dict.keys()} with the key items {my_dict.items()}')



# Write a Python Script to iterate over a dictionary using loops. (Use any dictionary as an example)
print("QUESTION FOUR SOLUTION")
print("----------------------------------------")
my_dict = {

    "brand": 'Ford',
    "Model": 'Mustang',
    "Year": "1964",
    "class": "First"

}
for key in my_dict.items():
    print(key)


# Write a Python program to sum up all the items in a list 
print("QUESTION FIVE SOLUTION")
print("----------------------------------------")
my_list = [34, 56, 78, 978, 45, 23, 46, 788, 24]
summation = (sum(my_list))
print(summation)



#  Write a Python program to multiply all the items in a list
print("QUESTION SIX SOLUTION")
print("----------------------------------------")
def mult(list):
    result = 1
    for elements in list:
        result = result * elements
    return result
listgiven = [1, 2, 3]
print(mult(listgiven))



# Write a Python program to get the largest number from the list
print("QUESTION SEVEN SOLUTION")
print("----------------------------------------")
my_list = [34, 56, 78, 978, 45, 23, 46, 788, 24]
highest = max(my_list)
print(highest)



# Write a Python program to get the lowest number from the list
print("QUESTION EIGHT SOLUTION")
print("----------------------------------------")
my_list = [34, 56, 78, 978, 45, 23, 46, 788, 24]
lowest = min(my_list)
print(lowest)