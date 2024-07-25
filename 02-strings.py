#Ask user for their name
name = input("Write your full name: ").strip().title()

#Split the user's name into first name and last name
first, last = name.split("")

#Say hello to the user

print(f"Hello!, {first}")

