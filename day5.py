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
