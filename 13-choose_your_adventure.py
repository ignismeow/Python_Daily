name = input("Please enter your name: ")

print(f'Welome {name}, You are about to go to adventure')

answer = input("You're about to climb a mount a deadly mountain, Do you wanna go ahead 'g' or quit 'q': ").lower()
if answer == 'q':
    print("You exited!")
elif answer == 'g':
    answer = input('move straight and go will see hidden glacier on the end do you wanna pass "p" the glcacier of die "d": ').lower()
    if answer == "p":
        print("You have passed and you are on top of mountain!")
    elif answer == "d":
        print("You are dead! Better luck next time.")
        quit()
    else:
        print('Please enter the suggested output.')
else:
    print('Please enter the suggested output.')

