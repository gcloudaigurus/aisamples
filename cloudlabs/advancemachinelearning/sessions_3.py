
# Import necessary libraries
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# Define the CNN model
model = Sequential([
  # Convolutional layer 1: 32 filters, 3x3 kernel size, ReLU activation
  Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)), #input_shape assumes 28x28 grayscale images
  # Max pooling layer 1: 2x2 pool size
  MaxPooling2D((2, 2)),
  # Convolutional layer 2: 64 filters, 3x3 kernel size, ReLU activation
  Conv2D(64, (3, 3), activation='relu'),
  # Max pooling layer 2: 2x2 pool size
  MaxPooling2D((2, 2)),
  # Flatten layer: converts the 2D feature maps to a 1D vector
  Flatten(),
  # Dense layer 1: 128 neurons, ReLU activation
  Dense(128, activation='relu'),
  # Output layer: 10 neurons (for 10 classes), softmax activation
  Dense(10, activation='softmax') #assuming 10 classes (e.g., digits 0-9)
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy', #Use sparse if labels are integers
              metrics=['accuracy'])

# Load and pre-process the MNIST dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0
x_train = x_train.reshape(-1,28,28,1) #Reshape to add channel dimension for grayscale
x_test = x_test.reshape(-1,28,28,1)

# Train the model
model.fit(x_train, y_train, epochs=5, batch_size=32) #adjust epochs and batch size as needed

# Evaluate the model
loss, accuracy = model.evaluate(x_test, y_test)
print('Test accuracy:', accuracy)


# Make predictions
predictions = model.predict(x_test)
#Example of getting the predicted class for the first test image:
predicted_class = tf.argmax(predictions[0]).numpy()
print(f"Predicted class for the first test image: {predicted_class}")


