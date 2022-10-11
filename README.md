# Python Introduction

## Why Python
- Easy to learn 
- Flexible
- Efficient, fast and reliable
- Libraries and frameworks
## Python Use Cases
- Web Applications
- Data Science
- Artificial Intelligence
- Game Development
- Data Analytics
## Python Variables
Variables are containers for storing data values
- `first_name = "Mohamed" - String`
- `DOB = 99 - Integer`
- `UK_resident = yes or no - Boolean`
- `travel = 15.4 - Float`

```python
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
```


## Localhost to GitHub
- Generate ssh key-pair on localhost
- Keep the private key on localhost inside .ssh folder
- Copy the public key into your repository on GitHub

![ssh-diagram](images/ssh-authentication.png)

# How to Set Up GitHub Using .ssh Keys

## Create GitHub SSH Keys
- The SSH keys you create for GitHub must go in the .ssh folder
- `mkdir .ssh`
- Generate a new set of keys
- `ssh-keygen -t rsa -b 4096 -C your@email.com`
- Add your SSH key to ssh-agent
```python
eval `ssh-agent -s`
ssh-agent -s
```
- Add your private key to ssh-agent
- `ssh-add ~/.ssh/id_rsa`
- Copy your public key to the clipboard
- `clip < ~/.ssh/id_rsa.pub`#
- Add your public SSH key to GitHub. Go to GitHub settings page and click the "New SSH key" button. Paste in your public (id_rsa.pub) key

![add-ssh-key](images/github-add-ssh-key.png)

## Git & GithHub
- Add changes to our GitHub repo
- `git add filename` or `git add .` - means push everyting from current location
- `git commit -m "new markdown guide added"`
- Now let's send this new data to GitHub
- `git push -u origin main`
<<<<<<< HEAD
- `git status`
=======
- `git status`
>>>>>>> 6c1c1f1b4d932754bd200ff0160251f9dec1bec9
- checking