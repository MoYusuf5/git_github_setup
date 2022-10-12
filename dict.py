# What is a Dictionary?
# How to manage Dictionaries - How to manage the data using Dict
# It works as Key value - 'pair key = value'
# Syntax `{   "Key" : "Value"   }`
#               0        1
# print(name[1])

# store student's data - name, course_name, progress, completed_lessons
students_1 = {
    "keys" : "values",
    "name" : "Mohamed",
    "stream" : "DevOps",
    "completed_lessons" : 4,
    "completed_lessons_names" : ["lists", "tuples", "OOP"]
                               #    0        1          2
}
print(students_1) # prints the list
print(type(students_1)) # prints the type of data collection
print(students_1["stream"]) # prints the value saved inside the 'stream' key

# print/display completed_lessons_names
print(students_1["completed_lessons_names"])

# # print/display completed_lessons_names index 0 means lists
print(students_1["completed_lessons_names"][0])

students_1["completed_lessons"] = 3 # changes the value of completed_lessons
print(students_1["completed_lessons"])

# Delete an item from the lists of completed_lessons_names / key
students_1["completed_lessons_names"].remove("OOP")
print(students_1["completed_lessons_names"])

# Dict Built In Methods
# displays keys only or values only
# keys() values()
print(students_1.keys()) # displays keys only from student_1
print(students_1.values()) # displays keys only from student_1











