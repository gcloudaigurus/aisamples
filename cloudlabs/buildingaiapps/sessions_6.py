
# This program demonstrates a simple neural network for binary classification using NumPy.
# It's a basic introduction and doesn't include advanced optimization or regularization techniques.

import numpy as np

# Sigmoid activation function
def sigmoid(x):
  """
  Applies the sigmoid function element-wise.
  """
  return 1 / (1 + np.exp(-x))

# Derivative of the sigmoid function
def sigmoid_derivative(x):
  """
  Calculates the derivative of the sigmoid function.
  """
  return x * (1 - x)

# Neural Network class
class NeuralNetwork:
  def __init__(self, input_size, hidden_size, output_size):
    """
    Initializes the neural network with random weights.
    """
    self.weights1 = np.random.randn(input_size, hidden_size)  # Weights between input and hidden layer
    self.bias1 = np.random.randn(1, hidden_size)             # Bias for hidden layer
    self.weights2 = np.random.randn(hidden_size, output_size) # Weights between hidden and output layer
    self.bias2 = np.random.randn(1, output_size)             # Bias for output layer

  def forward(self, X):
    """
    Performs the forward pass of the network.
    """
    self.hidden_layer_input = np.dot(X, self.weights1) + self.bias1
    self.hidden_layer_output = sigmoid(self.hidden_layer_input)
    self.output_layer_input = np.dot(self.hidden_layer_output, self.weights2) + self.bias2
    self.predicted_output = sigmoid(self.output_layer_input)
    return self.predicted_output

  def backward(self, X, y, output):
    """
    Performs the backward pass (backpropagation) to calculate gradients.
    """
    self.output_error = y - output
    self.output_delta = self.output_error * sigmoid_derivative(output)

    self.hidden_layer_error = self.output_delta.dot(self.weights2.T)
    self.hidden_layer_delta = self.hidden_layer_error * sigmoid_derivative(self.hidden_layer_output)

    self.weights2 += self.hidden_layer_output.T.dot(self.output_delta) * self.learning_rate
    self.bias2 += np.sum(self.output_delta, axis=0, keepdims=True) * self.learning_rate
    self.weights1 += X.T.dot(self.hidden_layer_delta) * self.learning_rate
    self.bias1 += np.sum(self.hidden_layer_delta, axis=0, keepdims=True) * self.learning_rate

  def train(self, X, y, epochs, learning_rate):
    """
    Trains the neural network using backpropagation.
    """
    self.learning_rate = learning_rate
    for i in range(epochs):
      output = self.forward(X)
      self.backward(X, y, output)
      # You might want to add a loss function calculation and printing here for monitoring progress.


# Example usage:
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]]) # Input data
y = np.array([[0], [1], [1], [0]]) # Target output (XOR gate)

nn = NeuralNetwork(input_size=2, hidden_size=2, output_size=1) # Initialize a 2-2-1 network
nn.train(X, y, epochs=10000, learning_rate=0.1) # Train the network

#Test the network
print("Predictions:")
print(nn.forward(X))


