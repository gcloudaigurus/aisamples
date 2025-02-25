
# Import necessary libraries
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Generate sample data (replace with your own data)
# This creates a dataset where y is linearly related to x with some added noise.
X = np.array([[1], [2], [3], [4], [5]])  # Features (independent variable)
y = np.array([2, 4, 5, 4, 5])  # Target (dependent variable)


# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) # 80% train, 20% test

# Create and train a linear regression model
model = LinearRegression() # Initialize the model.  Linear Regression is used because it is a simple and widely used regression algorithm.
model.fit(X_train, y_train) # Train the model using the training data. The fit method adjusts the model parameters to best fit the data.


# Make predictions on the test set
y_pred = model.predict(X_test) # Predict the target variable for the test data using the trained model.


# Evaluate the model
mse = mean_squared_error(y_test, y_pred) # Calculate the Mean Squared Error (MSE).  MSE measures the average squared difference between the predicted and actual values. Lower MSE indicates better performance.
r2 = r2_score(y_test, y_pred) # Calculate the R-squared (R²) score.  R² represents the proportion of variance in the dependent variable explained by the model.  Higher R² (closer to 1) indicates better fit.

# Print the evaluation metrics
print(f"Mean Squared Error (MSE): {mse}")
print(f"R-squared (R²): {r2}")

# Print the model's coefficients (slope and intercept)
print(f"Coefficients: {model.coef_}") # Model's slope
print(f"Intercept: {model.intercept_}") # Model's y-intercept

#Example of prediction on a new data point
new_data_point = np.array([[6]])
predicted_value = model.predict(new_data_point)
print(f"Prediction for new data point: {predicted_value}")


