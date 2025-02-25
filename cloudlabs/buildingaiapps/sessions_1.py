
# Introduction to AI Tools: A Simple Example using Python

# This program demonstrates basic AI concepts using readily available Python libraries.
# Specifically, we'll touch upon:
# 1. Data Manipulation with Pandas:  For handling structured data.
# 2. Machine Learning with Scikit-learn:  For building a simple model.


# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Sample Data:  Housing Prices (Simplified for demonstration)
# We'll predict house price based on size.
data = {'size': [1000, 1500, 1200, 1800, 2000], 
        'price': [200000, 300000, 250000, 350000, 400000]}

# Create a Pandas DataFrame
df = pd.DataFrame(data)

# 1. Data Manipulation (Pandas):
#    - The data is already simple, but Pandas would be crucial for larger, more complex datasets.
#    -  Here, we could add data cleaning, feature engineering steps if needed.

# 2. Machine Learning (Scikit-learn):
#    - We'll use a simple linear regression model to predict house price from size.

# Separate features (X) and target (y)
X = df[['size']] #Features
y = df['price'] # Target

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) #test_size = 20% of the data

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model (using Mean Squared Error)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# The MSE value indicates the average squared difference between the actual and predicted prices. 
# A lower MSE suggests better model performance.


#Further steps (not included for brevity but crucial in real-world AI):
# * More sophisticated model selection and hyperparameter tuning
# * Model evaluation using multiple metrics (e.g., R-squared, RMSE)
# * Data visualization to understand the data and model performance.
# * Handling larger datasets, missing data, and feature scaling.


