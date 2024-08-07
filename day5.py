#Problem: Write a python program to add new elements in the list
# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }

# Print out the capital of France
print(europe['france']['capital'])
# Create sub-dictionary data
data = {
    'capital': 'rome', 'population': 59.83
}
# Add data to europe under key 'italy'
europe['italy'] = data
# Print europe
print(europe)


#Problem: Compare boolean operators
# Comparison of booleans
print(True == False)
# Comparison of integers
print((-5*15) != 75)
# Comparison of strings
print('pyscript' == 'PyScript')
# Compare a boolean with an integer
print(True == 1)


#Problem: Solve comparison operators
my_kitchen = 18.0
your_kitchen = 14.0
# my_kitchen bigger than 10 and smaller than 18?
print(my_kitchen > 10 and my_kitchen < 18)
# my_kitchen smaller than 14 or bigger than 17?
print(my_kitchen < 14 or my_kitchen > 17)
# Double my_kitchen smaller than triple your_kitchen?
print(2*my_kitchen < 3*your_kitchen)


#Problem: if, else & elif statments
# Define variables
room = "kit"
area = 14.0
# if statement for room
if room == "kit" :
    print("looking around in the kitchen.")
# if statement for area
if area > 15:
    print("big place!")


# Define variables
room = "kit"
area = 14.0
# if-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
else :
    print("looking around elsewhere.")
# if-else construct for area
if area > 15 :
    print("big place!")
else:
    print("pretty small.")


# Define variables
room = "bed"
area = 14.0
# if-elif-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
elif room == "bed":
    print("looking around in the bedroom.")
else :
    print("looking around elsewhere.")
# if-elif-else construct for area
if area > 15 :
    print("big place!")
elif area > 10:
    print("medium size, nice!")
else :
    print("pretty small.")
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
# Convert code to a one-liner
sel = cars[cars['drives_right']]
# Print sel
print(sel)


## Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
# Create car_maniac: observations that have a cars_per_cap over 500
cpc = cars['cars_per_cap']
many_cars = cpc > 500
car_maniac = cars[many_cars]
# Print car_maniac
print(car_maniac)

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Import numpy, you'll need this
import numpy as np

# Create medium: observations with cars_per_cap between 100 and 500
cpc  = cars['cars_per_cap']
between = np.logical_and(cpc >= 100, cpc <= 500)
medium = cars[between]
# Print medium
print(medium)


# Initialize offset
offset = 8
# Code the while loop
while offset != 0:
    print("correcting...")
    offset = offset - 1


#Problem: Guess the Number Game:
import random
# should_continue = True
score = 0
random_number = random.randint(1, 10)
while True:
    guessed = int(input("Please guess the number here: "))
    if guessed > random_number:
        print("You guessed too high!")
        score += 1
    elif guessed < random_number:
        print("You guessed too low!")
        score += 1
    else:
        print(f"You guessed it right!, you total guess are {score}.")   
    user_input = input('Wanna try again?(y or q): ').lower()
    if user_input == 'q':
        # should_continue = False
        quit()


#Problem Madlib game:
Adjective = str(input("Please enter your Adjective: "))
Noun = str(input("Please enter your Noun: "))
Verb = str(input("Please enter your Verb: "))
Silly_name = str(input("Please enter your Silly_name: "))
Emotion = str(input("Please enter your Emotion: "))
He_she = str(input("Please enter your He_she: "))
story = f"""In a land far, far away, there lived a {Adjective} {Noun} named {Silly_name}. {Silly_name} lived in a {Noun} made of {Noun}. One day, while {Verb}, {Silly_name} stumbled upon a {Adjective} {Noun}.
Curious, {Silly_name} decided to {Verb}. Suddenly, the {Adjective} {Noun} started to {Verb}. {Silly_name}, feeling {Emotion}, {Verb} as fast as {He_she} could.
Just when {Silly_name} thought all hope was lost, a {Adjective} {Noun} appeared. The {Adjective} {Noun} helped {Silly_name} {Verb} the {Adjective} {Noun}.
Grateful, {Silly_name} thanked the {Adjective} {Noun} and they became the best of friends. From that day on, {Silly_name} and the {Adjective} {Noun} went on many more {Adjective} adventures together."""
print(story)
