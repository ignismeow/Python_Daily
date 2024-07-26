#Conditional Statements
> >= < <= == !=

x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")


#Using "or" statement
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y or x > y:
  print("x is not equal to y")
else:
  print("x is equal to y")


#Using != operator
x = int(input("What's x? "))
y = int(input("What's y? "))

if x != y:
  print("x is not equal to y")
else:
  print("x is equal to y")


#Using == operator
x = int(input("What's x? "))
y = int(input("What's y? "))

if x == y:
  print("x is equal to y")
else: 
  print("x is not equal to y")


#Using & operator
score = int(input("Score: "))

if score >=90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")
else score>:
