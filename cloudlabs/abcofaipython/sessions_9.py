
# Import necessary libraries
import numpy as np

# Define the sigmoid activation function
def sigmoid(x):
  """
  This function implements the sigmoid activation function.  
  It takes a single number or a NumPy array as input and returns its sigmoid.
  """
  return 1 / (1 + np.exp(-x))

# Define the sigmoid derivative function (needed for backpropagation)
def sigmoid_derivative(x):
  """
  Calculates the derivative of the sigmoid function.  Used in backpropagation.
  """
  return x * (1 - x)


# Define a simple neural network class
class NeuralNetwork:
  def __init__(self, input_size, hidden_size, output_size):
    """
    Initializes the neural network with random weights.
    input_size: number of input features
    hidden_size: number of neurons in the hidden layer
    output_size: number of output neurons
    """
    self.weights_input_hidden = np.random.rand(hidden_size, input_size) # Weights between input and hidden layer
    self.bias_hidden = np.random.rand(hidden_size, 1) # Biases for the hidden layer
    self.weights_hidden_output = np.random.rand(output_size, hidden_size) # Weights between hidden and output layer
    self.bias_output = np.random.rand(output_size, 1) # Biases for the output layer


  def forward_propagation(self, X):
    """
    Performs forward propagation to calculate the output of the network.
    X: Input data (NumPy array)
    """
    self.hidden_layer_input = np.dot(self.weights_input_hidden, X) + self.bias_hidden  # Calculate hidden layer input
    self.hidden_layer_output = sigmoid(self.hidden_layer_input) # Apply sigmoid activation to hidden layer
    self.output_layer_input = np.dot(self.weights_hidden_output, self.hidden_layer_output) + self.bias_output #Calculate output layer input
    self.predicted_output = sigmoid(self.output_layer_input) #Apply sigmoid activation to output layer. This is the network's prediction.
    return self.predicted_output


  def backpropagation(self, X, y, learning_rate):
    """
    Performs backpropagation to update the network's weights and biases.
    X: Input data
    y: True output
    learning_rate: Learning rate for weight updates
    """
    # Calculate output layer errors
    output_error = y - self.predicted_output
    d_output = output_error * sigmoid_derivative(self.predicted_output)

    # Calculate hidden layer errors
    hidden_error = np.dot(self.weights_hidden_output.T, d_output)
    d_hidden = hidden_error * sigmoid_derivative(self.hidden_layer_output)

    # Update weights and biases
    self.weights_hidden_output += learning_rate * np.dot(d_output, self.hidden_layer_output.T)
    self.bias_output += learning_rate * d_output
    self.weights_input_hidden += learning_rate * np.dot(d_hidden, X.T)
    self.bias_hidden += learning_rate * d_hidden



# Example usage:
# Initialize a neural network with 2 inputs, 2 neurons in the hidden layer, and 1 output neuron
nn = NeuralNetwork(2, 2, 1)

# Training data
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]]).T #Input data as columns. Note the transpose.
y = np.array([[0], [1], [1], [0]]) # Corresponding outputs


# Training loop
epochs = 10000
learning_rate = 0.1
for i in range(epochs):
  nn.forward_propagation(X)
  nn.backpropagation(X, y, learning_rate)


#Test the trained network
print("Predictions after training:")
print(nn.forward_propagation(X)) #Show the final predictions for the training data.  Expect values near [0,1,1,0]

