
# This program demonstrates a simple supervised learning example using linear regression.
# We'll predict house prices based on their size.

# Import necessary libraries
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Sample data: House size (in sq ft) and price (in thousands of dollars)
house_size = np.array([1000, 1500, 1200, 1800, 2000, 2500, 1600, 2200, 1400, 1900]).reshape((-1, 1)) # Reshape for sklearn
house_price = np.array([200, 300, 250, 350, 400, 500, 320, 450, 280, 380])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(house_size, house_price, test_size=0.2, random_state=42) # 80% train, 20% test

# Create and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train) # Training the model on training data

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Print the model's coefficients (slope and intercept)
print(f"Coefficients: {model.coef_}") #slope
print(f"Intercept: {model.intercept_}") #intercept


# Example prediction: Predict the price of a 1700 sq ft house.
new_house_size = np.array([[1700]])
predicted_price = model.predict(new_house_size)
print(f"Predicted price for a 1700 sq ft house: {predicted_price[0]}")

#This is a very basic example. Real-world applications involve more complex data, models, and evaluation metrics.

