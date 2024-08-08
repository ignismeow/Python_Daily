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
