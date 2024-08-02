# Problem 1
# level 1
l = []
for i in range(2000, 3201):
    if (i%7==0) & (i%5!=0):
        l.append(str(i))
        
print(l) 


# Problem 2
# level 1
name = input("Please Enter your name: ")
age = input("Please enter your age: ")
times = input("How many time you need message: ")

# years to 100
years_to_hundred = 100 - int(age)

message = f"Hello {name}!, Your'e {years_to_hundred} years away to reach hundred years old.\n"
message

print(type(message))

print(message*int(times))
