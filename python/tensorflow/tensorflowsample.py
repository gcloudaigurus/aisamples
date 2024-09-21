import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np

# Load and preprocess the MNIST dataset
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize the images to [0, 1] range
x_train, x_test = x_train / 255.0, x_test / 255.0

# Create a simple neural network model
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),  # Flatten the 28x28 images to a 1D vector
    layers.Dense(128, activation='relu'),  # First fully connected layer with ReLU activation
    layers.Dropout(0.2),                   # Dropout layer for regularization
    layers.Dense(10)                       # Output layer with 10 units (one for each digit)
])

# Compile the model
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=5)

# Evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print('\nTest accuracy:', test_acc)

# Add a softmax layer to convert the logits to probabilities
probability_model = models.Sequential([
    model,
    layers.Softmax()
])

# Use the model to make predictions
predictions = probability_model.predict(x_test)

# Print the prediction for the first test image
print('\nPrediction for the first test image:', np.argmax(predictions[0]))
print('Actual label for the first test image:', y_test[0])
