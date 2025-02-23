#This program demonstrates a simple neural network using TensorFlow/Keras to classify handwritten digits from the MNIST dataset.  It's a fundamental example, but showcases core deep learning concepts.

import tensorflow as tf
from tensorflow import keras
import numpy as np

# Load and pre-process the MNIST dataset
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0
x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)
y_train = keras.utils.to_categorical(y_train, num_classes=10)
y_test = keras.utils.to_categorical(y_test, num_classes=10)

# Define the neural network model
model = keras.Sequential([
    keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Conv2D(64, (3, 3), activation='relu'),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Flatten(),
    keras.layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=5, batch_size=32)

# Evaluate the model
loss, accuracy = model.evaluate(x_test, y_test)
print(f"Test accuracy: {accuracy}")

# Make predictions (optional)
predictions = model.predict(x_test)
print(f"Predictions shape: {predictions.shape}")  # Shape will be (10000, 10) - probabilities for each digit

#Example of getting the predicted digit for a specific image:
predicted_digit = np.argmax(predictions[0]) #get the index of the highest probability
print(f"Prediction for the first test image: {predicted_digit}")


#Before running this code:

#1. **Install TensorFlow:**  If you don't have it already, install it using pip:  `pip install tensorflow`

#2. **Ensure you have enough RAM:** MNIST is relatively small, but training larger models requires substantial RAM.

#This program uses a convolutional neural network (CNN), which is well-suited for image data like MNIST.  It includes:

#* **Data Loading and Preprocessing:** Loads the MNIST dataset, normalizes pixel values, and converts labels to one-hot encoding.
#* **Model Definition:** Creates a CNN with convolutional layers, max pooling, flattening, and a dense output layer.
#* **Model Compilation:** Specifies the optimizer, loss function, and metrics.
#* **Model Training:** Trains the model on the training data.
#* **Model Evaluation:** Evaluates the model's performance on the test data.
#* **Prediction Example:** Shows how to obtain predictions from the trained model.

#Remember that the accuracy might vary slightly on each run due to the stochastic nature of the training process.  You can experiment with different model architectures, hyperparameters (like the number of epochs or batch size), and optimizers to improve performance.  This example provides a solid foundation for exploring more advanced deep learning concepts.
