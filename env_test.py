# testing the env with print statement

# Python Variable?
# To store any data -
# To store user data - hard code the data - any other type
# first_name = "Mohamed" - String
# last_name = ""
# DOB = 99 - Int
# UK_resident = yes or no - Boolean
# salary = 40000
# travel = 15.4 - Float
# gross_salary = salary + travel

# first_name = "Mohamed"
# last_name = "Yusuf"
# salary = 50
# travel = 3.5

print(first_name + " " + last_name)
# display the value of var first_name and last_name
print(salary)
print(travel)

# How to find out the type of data stored in a variable
# type()
# print(type(travel))

# Interact with users by taking user data in - input()
# print("Good Morning, Please Enter Your Name")
# name = input() # took user input and stored in the var called name
# print(name) # then printed the user's name

print("Good Morning, Please Enter Your Full Name") # Get user first_name and last_name
full_name = input()
print("Enter Your DOB") # User DOB
d_o_b = input()
print("Enter Your Course Name") # Course name
course_name = input()
print("Are You a UK resident?") # UK_resident
uk_resident = input()

print(full_name)
print(d_o_b)
print(course_name)
print(uk_resident)