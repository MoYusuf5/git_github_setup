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
    "completed_lessons_names" : ["lists", "tuples", "strings"]
                               #    0        1          2
}
# print(students_1) # prints the list
# print(type(students_1)) # prints the type of data collection
# print(students_1["stream"]) # prints the value saved inside the 'stream' key

# print/display completed_lessons_names
print(students_1["completed_lessons_names"])

# print/display completed_lessons_names index 0 means lists
print(students_1["completed_lessons_names"][0])


