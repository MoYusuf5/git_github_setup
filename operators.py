# Let's see the operators in action

## Intro to Data Types and Operators
# - `+ - * /`

### Comparison Operators
# - `>` greater than
# - `<` less than
# - `==` equal to (True or False)
# - `>=` greater than or equal to
# - `<=` less than or equal to

# a = 24
# b = 16

# print(a + b) # outcome added value of a & b
# print(a - b) # outcome -a from b

# Comparison
# print(a > b) # True
# print(a < b) # False
# print(a == b) # False

# Built in methods in Python - Boolean Methods
# - DRY (Do Not Repeat Yourself)

# greeting = "Hello World!"
# print(greeting)
# print(greeting.isalpha())
# print(greeting.islower()) # checks if it is lower case
# print(greeting.startswith("H")) # checks if it starts with a specific character
# print(greeting.endswith("!")) # checks if it ends with a specific character

# String indexing - starts from 0
# Hello World!
# 0 1 2 3 4 5 6 7 8 9 10 11
# greeting = "Hello World!"
# print(greeting)
# # we have a built in method that checks the len of string
# print(len(greeting))
# print(greeting[1])
#
# # String Slicing
# print(greeting[0:5]) # prints Hello
# print(greeting[6:12]) # prints World!
#
# print(greeting[-12:-7]) # prints Hello
# print(greeting[-6:]) # prints World!

# String Methods Available
# Use Case - var = string "bsubfaubd        "

# white_space = "lot's of spaces at the end                 "
# print(len(white_space))
# # strip() removes the white blank spaces at the end of the string
# print(len(white_space.strip()))
#
# Example_text = "here's sOme text with lOt's of text"
# print(Example_text.count("text")) # counts how many times a word has been used in a string
# print(Example_text)
# print(Example_text.lower()) # converts the string to lower case
# print(Example_text.upper()) # converts the string to upper case
# print(Example_text.capitalize()) # capitalises the first character in a string
# print(Example_text.replace("with" , "," ))

# user data input
# first_name = "Mohamed"
# last_name = "Yusuf"
# salary = 40
#
# print(first_name)
# print(last_name)
# # print(first_name + " " + last_name + salary)
# print(first_name + " " + last_name + " " + str(salary)) # Cast by using the str function to convert an int to a str
# # F String
# print(f"Hello {first_name} {last_name}") # Only works with 3.5/6 or above

# TASK

print("Good Morning, Please Enter Your Full Name") # Get user first_name and last_name
full_name = input()
print("Enter Your DOB") # User DOB
d_o_b = input()
print("Enter Your Course Name") # Course name
course_name = input()
print("Are You a UK resident?") # UK_resident
uk_resident = input()
print("What is your door number?") # Door number
door_number = input()
print("What is your street address?") # Address
street_address = input()
print("What is your hobby?") # Hobby
hobby = input()

print(f"My name is {full_name}. I was born on {d_o_b}. I study {course_name}. A UK resident? {uk_resident}. I live at {door_number} {street_address}. My favourite hooby is {hobby}.")
