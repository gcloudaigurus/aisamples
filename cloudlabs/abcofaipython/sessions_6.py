
# Machine Learning Overview Sample Program

# This program demonstrates a simple linear regression using scikit-learn.
# Linear regression is a supervised learning algorithm used for predicting a continuous target variable.

# Import necessary libraries
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Generate some sample data (replace with your own data)
# X represents the features (input variables)
# y represents the target variable (output)
X = np.array([[1], [2], [3], [4], [5]])  
y = np.array([2, 4, 5, 4, 5])

# Split the data into training and testing sets
# This helps evaluate the model's performance on unseen data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) #test_size=0.2 means 20% for testing


# Create and train the linear regression model
model = LinearRegression()  # Initialize the model
model.fit(X_train, y_train) # Train the model using the training data


# Make predictions on the test set
y_pred = model.predict(X_test)


# Evaluate the model
mse = mean_squared_error(y_test, y_pred) #Calculate Mean Squared Error to evaluate the model
print(f"Mean Squared Error: {mse}")


# Print the model's coefficients (slope and intercept)
print(f"Coefficients: {model.coef_}") # model.coef_ gives the slope of the line
print(f"Intercept: {model.intercept_}") # model.intercept_ gives the y-intercept


#This is a basic example.  Real-world machine learning projects involve more complex datasets, 
#preprocessing steps (data cleaning, feature scaling, etc.), model selection, hyperparameter tuning,
#and more sophisticated evaluation metrics.  This example serves as an introduction to the basic concepts.
