# Creating a mad libs game for practice, done.

name = input("Enter a name: ")
theme = input("Enter some theme of party: ")
place = input("Enter a place: ")
day_of_week = input("Enter a day-of-week: ")
time = input("Enter a time: ")
verb = input("Enter any verb: ")
animal = input("Enter any animal name: ")
body_part = input("Enter any body part: ")


# Outputting the user according to his answers.

print(f"{name} is having a {theme} party.")
print(f"It's going to be at {place} on {day_of_week}.")
print(f"Please make sure to show up at {time}, or else ")
print(f"you will be required to {verb} a/an {animal} with your {body_part}")