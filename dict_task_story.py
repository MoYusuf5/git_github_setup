# Dictionary Basics

story_1 = {
    "start" : "On a cold morning there was a young boy named Harry Potter who discovered he was wizard",
    "middle" : "He went to a school of wizardry and came across the evil wizard, Lord Voldermort",
    "end" : "Finally, he defeated Voldermort and went on to live his life"
}

print(story_1) # prints entire dictionary
print(type(story_1)) # prints the type of the data collection
print(story_1.keys()) # prints only the keys
print(story_1.values()) # prints only the values
print(story_1["start"]) # prints the value of "start"
print(story_1["middle"]) # prints the value of "middle"
print(story_1["end"]) # # prints the value of "end"
story_1.update({"hero" : "yourSuperHero"}) # adds a new key:value pair
print(story_1)



