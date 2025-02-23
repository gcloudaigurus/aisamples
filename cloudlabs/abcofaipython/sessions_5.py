
# Import the matplotlib library
import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
x = np.linspace(0, 10, 100)  # 100 evenly spaced numbers from 0 to 10
y = np.sin(x) #Sine wave

# Create a simple line plot
plt.figure(figsize=(8, 6)) #Set figure size
plt.plot(x, y, label='sin(x)', color='blue', linewidth=2) #Plot the sine wave. label is for legend, color is for line color, linewidth is for line thickness

# Customize the plot
plt.title('Sine Wave Plot') #Title of the plot
plt.xlabel('x') #X-axis label
plt.ylabel('sin(x)') #Y-axis label
plt.grid(True)  # Add a grid to the plot for better readability
plt.legend() #Display the legend, which is specified by the label in the plt.plot function.


#Scatter Plot Example
np.random.seed(0) #Set random seed for reproducibility
x_scatter = np.random.rand(50) #Generate 50 random numbers between 0 and 1
y_scatter = np.random.rand(50) #Generate 50 random numbers between 0 and 1
plt.figure(figsize=(8,6)) #Creates a new figure for the scatter plot
plt.scatter(x_scatter,y_scatter, label='Random Data Points', color='red', marker='o', s=50) # s is the size of the marker.
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()


#Bar Chart Example
categories = ['A', 'B', 'C', 'D']
values = [25, 40, 15, 30]
plt.figure(figsize=(8,6))
plt.bar(categories, values, color=['green', 'orange', 'purple', 'brown'])
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')


#Show all plots
plt.show()
