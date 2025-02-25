
import numpy as np
import tensorflow as tf

# Define the RNN model
class RNN(tf.keras.Model):
  def __init__(self, vocab_size, embedding_dim, rnn_units):
    super().__init__(name="rnn_model")
    # Embedding layer to convert word indices to vectors
    self.embedding = tf.keras.layers.Embedding(vocab_size, embedding_dim)
    # SimpleRNN layer processes the sequence of word embeddings
    self.rnn = tf.keras.layers.SimpleRNN(rnn_units, return_sequences=True, return_state=True)
    # Dense layer for classification (or other output)
    self.dense = tf.keras.layers.Dense(1) #Example: binary classification

  def call(self, inputs, states=None):
    # Pass inputs through embedding layer
    x = self.embedding(inputs)
    # Pass embedded inputs through RNN layer
    if states is None:
      output, states = self.rnn(x)
    else:
      output, states = self.rnn(x, initial_state=states)
    # Pass RNN output through dense layer for prediction
    output = self.dense(output)
    return output, states


# Example usage:

# Define hyperparameters
vocab_size = 10000  # Size of vocabulary
embedding_dim = 256 # Dimension of word embeddings
rnn_units = 128     # Number of units in RNN layer
batch_size = 64     # Batch size for training

# Generate some sample data (replace with your actual data)
# This is just placeholder data for demonstration

num_samples = 1000
seq_length = 20
X_train = np.random.randint(0, vocab_size, size=(num_samples, seq_length))
y_train = np.random.randint(0, 2, size=(num_samples, seq_length, 1)) # Example: binary classification


# Create the RNN model
model = RNN(vocab_size, embedding_dim, rnn_units)

# Define optimizer and loss function
optimizer = tf.keras.optimizers.Adam()
loss_fn = tf.keras.losses.BinaryCrossentropy(from_logits=True) #For binary classification. Adjust based on your task


# Training loop
epochs = 10
for epoch in range(epochs):
  for batch in range(num_samples // batch_size):
    with tf.GradientTape() as tape:
      start = batch * batch_size
      end = (batch + 1) * batch_size
      batch_x = X_train[start:end]
      batch_y = y_train[start:end]
      #reshape to (batch_size, seq_len, 1) if needed depending on loss function
      
      predictions, _ = model(batch_x)
      loss = loss_fn(batch_y, predictions) #Compute loss

    grads = tape.gradient(loss, model.trainable_variables) #Compute gradients
    optimizer.apply_gradients(zip(grads, model.trainable_variables)) #Apply gradients


    print(f"Epoch:{epoch+1}, Batch: {batch+1}/{num_samples // batch_size}, Loss:{loss.numpy()}")


# After training, you can use the model to make predictions on new data.  Remember to replace placeholder data with your real dataset.

