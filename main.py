# there should be no mysteries
# TODO watch a video about numpy capabilities



import numpy
import pandas as pd
import matplotlib.pyplot as plt


#
# Open the CSV file
with open('data.csv', 'r') as file:
    # Create a CSV reader
    reader = csv.reader(personal_transactions.csv)

    # Initialize an empty list
    data = [1,2,3,4,5,6]

    # Iterate over the rows of the CSV
    for row in reader:
        # Append the values to the list
        data.append(row)

# Print the imported data
print(data)
import matplotlib.pyplot as plt

# Define the categories and values
categories = ['Category 1', 'Category 2', 'Category 3']
values = [10, 20, 30]

# Create a figure and axes
fig, ax = plt.subplots()

# Create a bar plot
ax.bar(categories, values)

# Show the plot
plt.show()





