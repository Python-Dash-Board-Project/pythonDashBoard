# there should be no mysteries
# TODO watch a video about numpy capabilities




# import numpy
import pandas as pd
import matplotlib.pyplot as plt

# load data from csv file
data_frame = pd.read_csv('personal_transactions')


def create_line_plot():
   # create x and y values
   data_frame.plot(x='Date', y='Amount')

   # add title and labels to graph
   plt.title('Goat graph')

   plt.xlabel('Date')
   plt.ylabel('Amount')

   # display plot
   plt.show()
def create_pie():
   # Data to plot
   labels = ['Platinum Card', 'Checking', 'Silver Card']
   # Size should be equal to the number of instances of each card
   sizes = data_frame['Card Type']
   # Size should be equal to the number of instances of each card
   colors = ['#ff9999', '#66b3ff', '#99ff99']

   # Create the pie chart
   plt.pie(sizes, labels=labels, colors=colors)

   # Add a title
   plt.title('Card type usage')

   # Show the plot
   plt.show()


# function calls
create_line_plot()
create_pie()




