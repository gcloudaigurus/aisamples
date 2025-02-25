
# Advanced Topics: Model Optimization and Tuning

# This program demonstrates model optimization and tuning using scikit-learn's RandomForestRegressor.
# We'll use GridSearchCV for hyperparameter tuning and explore different optimization strategies.

import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.datasets import make_regression


# Generate sample data
X, y = make_regression(n_samples=100, n_features=10, noise=0.1, random_state=42)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Define the model
model = RandomForestRegressor(random_state=42)

# Define the hyperparameter grid for tuning
param_grid = {
    'n_estimators': [50, 100, 200],  # Number of trees in the forest
    'max_depth': [None, 10, 20],      # Maximum depth of the trees
    'min_samples_split': [2, 5, 10],  # Minimum samples required to split an internal node
    'min_samples_leaf': [1, 2, 4]     # Minimum samples required to be at a leaf node
}

# Perform GridSearchCV for hyperparameter tuning
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, scoring='neg_mean_squared_error', n_jobs=-1) #n_jobs=-1 uses all processors
grid_search.fit(X_train, y_train)


# Get the best model and its hyperparameters
best_model = grid_search.best_estimator_
best_params = grid_search.best_params_

# Make predictions on the test set
y_pred = best_model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print the results
print(f"Best Hyperparameters: {best_params}")
print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")


#Further Optimization (Example: RandomizedSearchCV for larger parameter space)

# from sklearn.model_selection import RandomizedSearchCV
# from scipy.stats import randint, uniform

# param_distributions = {
#     'n_estimators': randint(50, 200),
#     'max_depth': [None] + list(np.arange(10, 101, 10)),
#     'min_samples_split': randint(2, 20),
#     'min_samples_leaf': randint(1, 10)
# }

# random_search = RandomizedSearchCV(estimator=model, param_distributions=param_distributions, n_iter=20, cv=5, scoring='neg_mean_squared_error', n_jobs=-1, random_state=42)
# random_search.fit(X_train, y_train)

# best_model_random = random_search.best_estimator_
# best_params_random = random_search.best_params_

# y_pred_random = best_model_random.predict(X_test)
# mse_random = mean_squared_error(y_test, y_pred_random)
# r2_random = r2_score(y_test, y_pred_random)

# print("\nRandomizedSearchCV Results:")
# print(f"Best Hyperparameters: {best_params_random}")
# print(f"Mean Squared Error: {mse_random}")
# print(f"R-squared: {r2_random}")


