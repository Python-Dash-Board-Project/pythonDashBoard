# Sammy Hasan-Silva
import pandas as pd
import matplotlib.pyplot as plt


# load data from csv file
data_frame = pd.read_csv('personal_transactions')

# changes visual style
plt.style.use('bmh')


def create_line_plot():
    # create x and y values
    data_frame.plot(x='Date', y='Amount')

    # add title and labels to graph
    plt.title('Transaction costs over a lifetime')

    plt.xlabel('Date')
    plt.ylabel('Amount')

    # display plot
    plt.show()

    # todo make this for each month
def create_bar():

    # Extract the data
    x = data_frame['Account Type']
    y = data_frame['Amount']

    # todo flip x and y**
    plt.xlabel('Account Type')
    plt.ylabel('Amount Spent ($)')
    plt.bar(x, y)

    # Add a title
    plt.title('Total Spending by Account Type')

    # Show the plot
    plt.show()
def create_pie():
    # x = data_frame['Account Type']
    # y = data_frame['Amount']
    #
    # plt.pie(y, labels=x, radius=4, shadow=1)
    # # explode=[]


    labels = ['A', 'B', 'C', 'D']
    sizes = [15, 30, 45, 10]

    # Create the pie chart
    plt.pie(sizes, labels=labels)
    plt.title('testing output:')

    # Show the plot
    plt.show()
def scatter_plot():
    x = data_frame['Date']
    y = data_frame['Amount']

    plt.title('Distribution of transaction costs over a life time')
    plt.xlabel('Time')
    plt.ylabel('Cost ($)')

    plt.scatter(x,y)
    plt.show()

# function calls
scatter_plot()
create_bar()
create_line_plot()


#create_pie()

# CONCLUSIONS:
# line plot not as useful as scatter plot
# for this creating meaning from the transaction costs over a lifetime

# pie chart also not too useful for this dataset until I can classify dates into months/other classifications etc.






