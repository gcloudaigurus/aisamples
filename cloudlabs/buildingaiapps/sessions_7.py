
# Import necessary libraries
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense, Flatten
import numpy as np

# Define the image classification model
# We'll use a simple sequential model for this example.  More complex models 
# are possible and often necessary for better accuracy.
model = keras.Sequential([
  Flatten(input_shape=(28, 28)), # Flatten the 28x28 images into a 784-dimensional vector
  Dense(128, activation='relu'), # A fully connected layer with 128 neurons and ReLU activation
  Dense(10, activation='softmax') # Output layer with 10 neurons (for 10 classes, e.g., digits 0-9) and softmax activation for probabilities
])

# Compile the model
# We use the Adam optimizer, sparse categorical crossentropy loss function (for integer labels),
# and accuracy as the metric.
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Load the MNIST dataset
# MNIST is a built-in dataset in Keras, consisting of handwritten digits.
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Preprocess the data
# Normalize pixel values to be between 0 and 1.
x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255

# Train the model
# We train for 5 epochs.  More epochs might improve accuracy but increase training time.
model.fit(x_train, y_train, epochs=5)

# Evaluate the model
# Evaluate the model's performance on the test set.
loss, accuracy = model.evaluate(x_test, y_test)
print(f"Test accuracy: {accuracy}")

# Make a prediction
# Predict the class of a single image from the test set.
prediction = model.predict(np.expand_dims(x_test[0], axis=0))
predicted_class = np.argmax(prediction)
print(f"Predicted class: {predicted_class}")
print(f"Actual class: {y_test[0]}")


# Note: This is a very basic example.  For real-world applications, you'll need 
# to consider more sophisticated architectures, data augmentation, hyperparameter tuning, etc.
#  You might also need to install TensorFlow: `pip install tensorflow`

