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
