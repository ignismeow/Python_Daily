import random

top_of_range = input("Please input a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print('Please type a number larger than 0 next time.')
    quit()

# r = random.randrange(-5, 11)
random_number = random.randint(0, top_of_range)

guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time again')
        continue
    if user_guess == random_number:
        print("You guessed it right!")
        break
    elif user_guess > random_number:
        print("You guessed more than the number.")
    else:
        print("You guessed less then the number.")
        
        

print(f"You got it in {guesses} guesses.")
