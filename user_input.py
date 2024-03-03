# prompt: Create a new Python file and name it "user_input.py" Use the input() function to ask the user for their name and store it in a variable called "name". Use the input() function to ask the user for their age and store it in a variable called "age". Use the input() function to ask the user for their location and store it in a variable called "location". Print out a personalized message using the user.

%%writefile user_input.py

name = input("What is your name? ")
age = input("How old are you? ")
location = input("Where do you live? ")

print(f"Hello {name}, you are {age} years old and you live in {location}.")
