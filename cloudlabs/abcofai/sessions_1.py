#This program demonstrates a simple AI concept:  **linear regression** for predicting house prices based on size.  It's a foundational concept in machine learning, easily understandable for an introduction to AI.


import numpy as np
import matplotlib.pyplot as plt

# Sample data: House size (sq ft) and price (thousands of dollars)
house_sizes = np.array([1000, 1500, 1200, 1800, 2000, 2500])
house_prices = np.array([200, 300, 250, 350, 400, 500])


# Linear Regression:  Find the best-fitting line (y = mx + c)
# We'll use a simple approach (not using scikit-learn for simplicity)

# Calculate the means
x_mean = np.mean(house_sizes)
y_mean = np.mean(house_prices)

# Calculate the slope (m)
numerator = np.sum((house_sizes - x_mean) * (house_prices - y_mean))
denominator = np.sum((house_sizes - x_mean)**2)
slope = numerator / denominator

# Calculate the y-intercept (c)
y_intercept = y_mean - slope * x_mean

# Print the equation of the line
print(f"Equation of the line: y = {slope:.2f}x + {y_intercept:.2f}")


# Prediction:  Predict the price of a 1700 sq ft house
predicted_price = slope * 1700 + y_intercept
print(f"Predicted price for a 1700 sq ft house: ${predicted_price:.2f} thousand")


# Visualization (optional but helpful)
plt.scatter(house_sizes, house_prices, label='Data Points')
plt.plot(house_sizes, slope * house_sizes + y_intercept, color='red', label='Regression Line')
plt.xlabel('House Size (sq ft)')
plt.ylabel('House Price (thousands of $)')
plt.title('Simple Linear Regression')
plt.legend()
plt.show()



#This program does the following:

#1. **Imports necessary libraries:** `numpy` for numerical operations and `matplotlib` for plotting.
#2. **Defines sample data:**  House sizes and corresponding prices.  This is the "training data" the model learns from.
#3. **Performs linear regression:** Calculates the slope and y-intercept of the best-fitting line using the formula derived from least squares method.  This line represents the relationship between house size and price.
#4. **Makes a prediction:** Uses the calculated equation to predict the price of a house with a given size (1700 sq ft).
#5. **Visualizes the results:** Creates a scatter plot of the data points and overlays the regression line to show the model's fit.

#To run this code, make sure you have `numpy` and `matplotlib` installed (`pip install numpy matplotlib`).  Then, simply run the Python script.  The output will show the equation of the line, the prediction, and a plot visualizing the relationship.  This illustrates a very basic form of AI –  using data to learn a relationship and make predictions.  More complex AI models build upon similar principles but with much more sophisticated algorithms and larger datasets.
