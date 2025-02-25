
# Import necessary libraries
import numpy as np
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


# Generate sample data (replace with your own data)
X = np.random.rand(100, 10)  # 100 samples, 10 features
y = np.random.randint(0, 2, 100)  # Binary classification


# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) # 80% train, 20% test


# Define the model
model = RandomForestClassifier(random_state=42) # Initialize RandomForestClassifier


# Define the hyperparameter grid to search
param_grid = {
    'n_estimators': [50, 100, 200],  # Number of trees in the forest
    'max_depth': [None, 10, 20],      # Maximum depth of each tree
    'min_samples_split': [2, 5, 10],   # Minimum samples required to split an internal node
    'min_samples_leaf': [1, 2, 4]      # Minimum samples required to be at a leaf node
}


# Perform GridSearchCV for hyperparameter tuning
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, scoring='accuracy', n_jobs=-1) # 5-fold cross-validation
grid_search.fit(X_train, y_train) # Fit the model with the hyperparameter grid


# Get the best hyperparameters and model
best_params = grid_search.best_params_
best_model = grid_search.best_estimator_


# Evaluate the best model on the test set
y_pred = best_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)


# Print results
print("Best Hyperparameters:", best_params)
print("Test Accuracy:", accuracy)
print("Classification Report:\n", report)


