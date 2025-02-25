
# Import necessary libraries
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# Generate sample data (replace with your own dataset)
# This creates a synthetic dataset for demonstration.  In a real-world scenario, you would load your data from a file (e.g., CSV).
np.random.seed(42) # for reproducibility
X = np.random.rand(100, 2) * 10  # 100 samples, 2 features
y = np.array([1 if x[0] + x[1] > 7 else 0 for x in X]) # Simple classification rule


# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) # 80% train, 20% test


# Feature scaling (important for many algorithms like Logistic Regression)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test) # Apply the same scaling to test data


# Choose a classification model (Logistic Regression in this example)
model = LogisticRegression()


# Train the model
model.fit(X_train, y_train)


# Make predictions on the test set
y_pred = model.predict(X_test)


# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)


# Print the evaluation metrics
print(f"Accuracy: {accuracy}")
print(f"Confusion Matrix:\n{conf_matrix}")
print(f"Classification Report:\n{class_report}")


