# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
print(cars)
# Adapt for loop
for lab, row in cars.iterrows() :
    print(f"{lab}: {row['cars_per_cap']}")


# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
# Code for loop that adds COUNTRY column
cars['COUNTRY'] = [country.upper() for country in cars['country']]
# Print cars
print(cars)

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
# Use .apply(str.upper)
for lab, row in cars.iterrows() :
    cars['COUNTRY'] = cars['country'].apply(str.upper)
print(cars)

# Import numpy as np
import numpy as np
# Set the seed
np.random.seed(123)
# Generate and print random float
print(float(np.random.rand()))


# Import numpy and set seed
import numpy as np
np.random.seed(123)
# Use randint() to simulate a dice
print(np.random.randint(1, 7))
# Use randint() again
print(np.random.randint(1, 7))


# NumPy is imported, seed is set
# Starting step
step = 50
# Roll the dice
dice = np.random.randint(1, 7)
# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice <= 5 :
    step += 1
else:
    step = step + np.random.randint(1,7)
# Print out dice and step
print(step)
print(dice)


# NumPy is imported, seed is set
# Initialize random_walk
random_walk = [0]
# Complete the ___
for x in range(100) :
    # Set step: last element in random_walk
    step = random_walk[-1]
    # Roll the dice
    dice = np.random.randint(1,7)
    # Determine next step
    if dice <= 2:
        step = step - 1
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)
    # append next_step to random_walk
    random_walk.append(step)
# Print random_walk
print(random_walk)


# NumPy is imported, seed is set
# Initialize random_walk
random_walk = [0]
for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)
    if dice <= 2:
        # Replace below: use max to make sure step can't go below 0
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)
    random_walk.append(step)
print(random_walk)


# NumPy is imported, seed is set
# Initialization
random_walk = [0]
for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)
    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)
    random_walk.append(step)
# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
# Plot random_walk
plt.plot(random_walk)
# Show the plot
plt.show()


# NumPy is imported; seed is set
# Initialize all_walks (don't change this line)
all_walks = []
# Simulate random walk five times
for i in range(5) :
    # Code from before
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)
    # Append random_walk to all_walks
    all_walks.append(random_walk)
# Print all_walks
print(all_walks)


# numpy and matplotlib imported, seed set.
# initialize and populate all_walks
all_walks = []
for i in range(5) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)
    all_walks.append(random_walk)
# Convert all_walks to NumPy array: np_aw
np_aw = np.array(all_walks)
# Plot np_aw and show
plt.plot(np_aw)
plt.show()
# Clear the figure
plt.clf()
# Transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw)
# Plot np_aw_t and show
plt.plot(np_aw_t)
plt.show()


# numpy and matplotlib imported, seed set
# clear the plot so it doesn't get cluttered if you run this many times
plt.clf()
# Simulate random walk 20 times
all_walks = []
for i in range(20) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        # Implement clumsiness
        if np.random.rand() < 0.005 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)
# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))
plt.plot(np_aw_t)
plt.show()

# Series to dataframe
sr = {'s':pd.Series([1,2,3,4]), 'r':pd.Series([1,2,3,4])}
sr_data = pd.DataFrame(sr)
print(sr_data)

# List to dataframe
list = [[1,2,3,4,4],[11,12,13,14,15]]
list_dataframe = pd.DataFrame(list)
print(type(list_dataframe))
print(list_dataframe)

# Pandas Series
a_data = pd.Series(a, index = ["x", "y", "z"], dtype=float, name="a_data")
type(a_data)
print(a_data)
s1 = pd.Series(12, index=[1,2,3,4,5,6,7])
s2 = pd.Series(12, index=[1,2,3,4])
print(s1 + s2)


# Pandas to dic
dic = {
    'name': ['python', 'c', 'c++', 'java'],
    'por': [12, 13, 24, 25],
    'rank':[1, 4, 5, 2]
}
dic_data = pd.DataFrame(dic, columns=['name', 'rank'])
a_data = pd.DataFrame(a)
print(dic_data)
print(dic['name'])


#Pandas Addition and subtraction
var = pd.DataFrame({'A': [1,2,3,4], 'B':[5,6,7,8]})
var['addition'] = var['A']+var['B']
var['subtraction'] = var['A']-var['B']
print(var)
# Pnadas Greater then and less then
var = pd.DataFrame({'A':[10,20,30,40], 'B':[15,16,17,18]})
var['python'] = var['A'] <= 20
var['python_1'] = var['A'] >= 16
print(var)

# Pandas using insert function
var = pd.DataFrame({'A':[10,20,30,40], 'B':[15,16,17,18]})
var['python'] = var['A'] <= 20
var['python_1'] = var['A'] >= 16
var.insert(1, "python", var['A'])
var.insert(1, "python_1", [11,12,13,14])
var['python_12'] = var['A'][:3]
var1 = var.pop('python_12')
print(var)
# Pandas using del function
del var['python_12']
print(var)


# Pandas making a csv file
dic = {'a': [1,2,3,4,5,6], 's':[1,2,3,4,5,6]} 
d = pd.DataFrame(dic)
print(d)
d.to_csv("test2.csv", index=False, header=[1,2])
