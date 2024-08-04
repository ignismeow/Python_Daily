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

#Problem 4: Write a python program to find the larges among three numbers
#using lists
num_list = []
num_first = int(input("Please enter first number: "))
num_second = int(input("Please enter second number: "))
num_third = int(input("Please enter third number: "))
num_list.append(num_first)
num_list.append(num_second)
num_list.append(num_third)
largest_number = max(num_list)
print(f"The largest number is {largest_number}.")

#using if & else
num_first = int(input("Please enter first number: "))
num_second = int(input("Please enter second number: "))
num_third = int(input("Please enter third number: "))
if num_second < num_first > num_third:
    print(f"{num_first} is the largest number in the list.")
elif num_first < num_second > num_third:
    print(f"{num_second} is the largest number in the list.")
else:
    print(f"{num_third} is the largest number in the list.")

#Problem 5: Write a python program to check prime numbers
num = int(input("Please enter a number: "))
if  num <= 1:
    print("Please enter valid number! Try Again")
elif num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime Pumber")
            break
    else:
        print("Prime Number")

#Problem 6: Write a python program to generate random number
import random
random_number = random.randint(1, 6)
print(random_number)

#Problem 7: Write a python program to print all the prime numbers in an interval
num_first = int(input("Please enter first number: "))
num_last = int(input("Please enter last number: "))
# if num_first <= 1 or num_last <=1:
#     print("Please enter a valid range of numbers Please!")
for num in range(num_first, num_last + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
    
    elif num <= 1:
        print("1 or less then 1 are not prime numbers.")

#Problem 8: Write a python program to convert celcius to forenheit
celcius = float(input("Please temperature in °C: "))
forenheit = (celcius * 1.8) + 32
message = f"The given {celcius}°C in temperature is equal to {forenheit}°F"
print(message)

#Problem 9: Write a python program to find factorial of a number

num = int(input("Please enter a number: "))
factorial = 1
if num < 0:
    print("Factorial of number below zero does not exits!")
elif num == 0:
    print("Factorial of 0 is", 1)
    quit()
if num > 1:
    for i in range(1, num+1):
        factorial *= i
print(factorial)

#method using recurssion method
def fact(a):
    if a == 0:
        return 1
    else:
        return ((a)*fact(a-1))

num = int(input("Please enter number here: "))
print(f"The factorial of given number is {fact(num)}.")
