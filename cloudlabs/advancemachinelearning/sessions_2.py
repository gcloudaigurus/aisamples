
# Deep Learning Architectures I: Neural Networks - Sample Program

# This program demonstrates a simple feedforward neural network 
# using the TensorFlow/Keras library.  It's designed for educational purposes
# and showcases basic concepts like model creation, compilation, training, and evaluation.

# Import necessary libraries
import tensorflow as tf
import numpy as np

# Define the model architecture
model = tf.keras.Sequential([
    # Input layer with 784 features (e.g., 28x28 image flattened)
    tf.keras.layers.Flatten(input_shape=(784,)),  
    # Hidden layer with 128 neurons and ReLU activation
    tf.keras.layers.Dense(128, activation='relu'),  
    # Output layer with 10 neurons (e.g., for 10 digit classification) and softmax activation
    tf.keras.layers.Dense(10, activation='softmax') 
])

# Compile the model
# Adam is a popular optimization algorithm
# SparseCategoricalCrossentropy is suitable for multi-class classification with integer labels
# Metrics like accuracy are used to track performance during training
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Generate some sample data for demonstration
# In a real-world scenario, you'd load your own dataset
num_samples = 1000
img_height, img_width = 28, 28
x_train = np.random.rand(num_samples, img_height*img_width) #random input data
y_train = np.random.randint(0, 10, num_samples) #random labels (0-9)


# Train the model
# epochs specifies the number of times the entire dataset is passed through the network
# batch_size determines the number of samples processed before updating the model's weights
model.fit(x_train, y_train, epochs=10, batch_size=32)

# Evaluate the model (on the training data in this simple example)
loss, accuracy = model.evaluate(x_train, y_train)
print(f"Loss: {loss:.4f}, Accuracy: {accuracy:.4f}")

# Make predictions (again, on training data for simplicity)
predictions = model.predict(x_train)
#predictions will be probabilities for each class (0-9)


# Note: This is a very basic example.  Real-world applications involve 
# data preprocessing, more complex architectures, hyperparameter tuning, 
# and evaluation on separate test sets to avoid overfitting.  
# Consider exploring more advanced techniques like convolutional neural networks (CNNs)
# for image data and recurrent neural networks (RNNs) for sequential data.

