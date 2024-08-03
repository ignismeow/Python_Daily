#Problem 1: Write a python program that calculates leap year
year = int(input("Please enter any year: "))
if (year % 400 == 0) & (year % 100 == 0):
    print(f"The year {year} is a leap year in all centuries.")
elif (year % 4 == 0) and (year % 100 != 0): 
    print(f"The year {year} is a leap year in one century.")
else:
    print(f"The year {year} is not a leap year.")

#Problem 2: Store names of some friends in list called name, print each name once at a time, send each of them personalized message, make a list of your favourite transportation vehicles and make a statment using this list items
names = ["Asad", "Ali", "Umer", "Agha"]
print(names[0]) #one way
print(names[1])
print(names[2])
print(names[3])

for name in names: # other way
    print(f"{name} you are a legend in this industry.")


Vehicles = ["Rubicon", "Ferrari", "Rolls Royce", "lamborgini"]
for vehicle in Vehicles:
    print(f"My second priority is {vehicle}")

#Problem 3: Store names of some friends in list called name, print each name once at a time, send each of them personalized message, make a list of your favourite transportation vehicles and make a statment using this list items
names = ["Asad", "Ali", "Umer", "Agha"]
print(names[0]) #one way
print(names[1])
print(names[2])
print(names[3])

#Problem 3.1: Change the list of guests name
names.remove("Ali")
names.remove("Agha")
names.insert(1, "Saad")
names.insert(3, "Fawad")
print(f"{names.pop()} Thanks for your presence I really appreciate that.")
del names[2]
print(names)

for name in names: # other way
    print(f"{name} you are really close to me I really like to hang out with you I want you to spare some precious time and come to my event, Please!")

#Problem 3.2:
Vehicles = ["Rubicon", "Ferrari", "Rolls Royce", "lamborgini"]
del Vehicles[3]
Vehicles.insert(1,"Fortuner")
Vehicles.pop(1)
Vehicles.remove('Rubicon')
print(Vehicles)
for vehicle in Vehicles:
    print(f"My second priority is {vehicle}.")
