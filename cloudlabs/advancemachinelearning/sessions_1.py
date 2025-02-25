
# Introduction to Advanced Machine Learning Concepts:  Illustrative Example

# This program demonstrates a few advanced concepts using a simplified example.  
#  It focuses on illustrating the ideas rather than building a production-ready model.


import numpy as np
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt


# 1. Data Generation and Preprocessing:  Creating a non-linearly separable dataset

# We use the make_moons function to generate a dataset with two classes that are not linearly separable.
X, y = make_moons(n_samples=200, noise=0.2, random_state=42) #random_state for reproducibility


# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# 2. Model Selection and Training: Comparing different model types

# A. Random Forest (Ensemble Method): Combines multiple decision trees to improve accuracy and robustness.
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42) #n_estimators is the number of trees
rf_classifier.fit(X_train, y_train)


# B. Support Vector Machine (SVM) with a non-linear kernel:  Handles non-linearly separable data effectively.
svm_classifier = SVC(kernel='rbf', gamma='scale', random_state=42) #'rbf' is a common kernel for non-linear data.
svm_classifier.fit(X_train, y_train)


# 3. Model Evaluation: Assessing the performance of the trained models

# Predict on the test set for both models
rf_predictions = rf_classifier.predict(X_test)
svm_predictions = svm_classifier.predict(X_test)


# Evaluate using accuracy, classification report, and confusion matrix
print("Random Forest:")
print("Accuracy:", accuracy_score(y_test, rf_predictions))
print(classification_report(y_test, rf_predictions))
print(confusion_matrix(y_test, rf_predictions))
print("\nSupport Vector Machine:")
print("Accuracy:", accuracy_score(y_test, svm_predictions))
print(classification_report(y_test, svm_predictions))
print(confusion_matrix(y_test, svm_predictions))


# 4. Visualization (Optional):  Visualizing the decision boundaries (for simpler datasets)

# Function to plot decision boundaries
def plot_decision_boundary(classifier, X, y, title):
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, 0.1))
    Z = classifier.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, alpha=0.8)
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k')
    plt.title(title)
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")



plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plot_decision_boundary(rf_classifier, X, y, "Random Forest Decision Boundary")
plt.subplot(1, 2, 2)
plot_decision_boundary(svm_classifier, X, y, "SVM Decision Boundary")
plt.show()


#Further exploration could include: Hyperparameter tuning (GridSearchCV, RandomizedSearchCV), cross-validation techniques, dimensionality reduction (PCA), dealing with imbalanced datasets, and more sophisticated model architectures (deep learning).

