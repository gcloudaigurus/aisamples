
# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler #for feature scaling


# Load the dataset (replace 'your_dataset.csv' with your actual file path)
data = pd.read_csv('your_dataset.csv') # Example:  A dataset with features (X) and target (y)

# Separate features (X) and target variable (y)
# Assumes your dataset has a column named 'target' as your dependent variable. Adjust accordingly
X = data.drop('target', axis=1) 
y = data['target']

#Handle missing values (if any).  Replace with your preferred method.
#Example: dropping rows with missing values
X = X.dropna()
y = y.dropna()


#Scale features using StandardScaler
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) # 80% train, 20% test

# Create and train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print the evaluation metrics
print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")


#Example of using other regression models (requires additional imports if not already imported)
# from sklearn.tree import DecisionTreeRegressor
# model = DecisionTreeRegressor()
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# mse = mean_squared_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)
# print(f"Decision Tree - Mean Squared Error: {mse}")
# print(f"Decision Tree - R-squared: {r2}")

#Remember to install required libraries:  pip install numpy pandas scikit-learn

