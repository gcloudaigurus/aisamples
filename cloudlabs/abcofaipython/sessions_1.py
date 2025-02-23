
# Introduction to AI in Python: A Simple Linear Regression Example

# This program demonstrates a basic linear regression model using the scikit-learn library.
# Linear regression is a fundamental supervised learning algorithm used for predicting a continuous target variable based on one or more predictor variables.

# Import necessary libraries
import numpy as np #NumPy for numerical operations, especially array handling
from sklearn.linear_model import LinearRegression #Scikit-learn for the Linear Regression model
from sklearn.model_selection import train_test_split #For splitting data into training and testing sets


# Generate sample data (replace with your own dataset if needed)
X = np.array([[1], [2], [3], [4], [5]])  #Independent Variable (Feature)
y = np.array([2, 4, 5, 4, 5]) #Dependent Variable (Target)


# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) #test_size determines the proportion of data for testing, random_state ensures reproducibility

# Create and train the linear regression model
model = LinearRegression() #creates a linear regression object
model.fit(X_train, y_train) #trains the model using the training data


# Make predictions on the test set
y_pred = model.predict(X_test) #makes predictions on the test data using the trained model


# Evaluate the model (a simple example, more sophisticated metrics exist)
#In a real-world scenario, you would use more robust evaluation metrics
print("Predictions:", y_pred)
print("Actual Values:", y_test)


# Get the model's coefficients (slope and intercept)
print("Intercept:", model.intercept_) #the y-intercept of the regression line
print("Coefficient:", model.coef_)  #the slope of the regression line

#This shows how the model has learned a relationship between X and y.  A more complete example would involve using more sophisticated evaluation metrics.

