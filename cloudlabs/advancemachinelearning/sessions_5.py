
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Define the encoder part of the autoencoder
# This encoder uses two dense layers to reduce the dimensionality of the input data.
# The activation function 'relu' introduces non-linearity.
encoder_inputs = keras.Input(shape=(28, 28, 1)) #input shape for MNIST images
x = layers.Conv2D(32, (3, 3), activation='relu', strides=2, padding='same')(encoder_inputs)
x = layers.Conv2D(64, (3, 3), activation='relu', strides=2, padding='same')(x)
# latent_dim represents the dimensionality of the latent space (compressed representation)
latent_dim = 16
# Flatten the output of the convolutional layers before feeding it to the dense layer.
shape_before_flattening = tf.shape(x)[1:]
x = layers.Flatten()(x)
latent_vector = layers.Dense(latent_dim, name="latent_vector")(x)  #latent vector is the compressed representation


# Define the decoder part of the autoencoder.
# This decoder mirrors the encoder, reconstructing the original input from the latent vector.
# The decoder uses the same architecture as the encoder, but in reverse order.
latent_inputs = keras.Input(shape=(latent_dim,))
x = layers.Dense(np.prod(shape_before_flattening))(latent_inputs)
x = layers.Reshape(shape_before_flattening)(x)
x = layers.Conv2DTranspose(64, (3, 3), activation='relu', strides=2, padding='same')(x)
x = layers.Conv2DTranspose(32, (3, 3), activation='relu', strides=2, padding='same')(x)
decoder_outputs = layers.Conv2DTranspose(1, (3, 3), activation='sigmoid', padding='same')(x) # output layer with sigmoid activation to produce probabilities


# Combine encoder and decoder to create the autoencoder model
encoder = keras.Model(encoder_inputs, latent_vector, name="encoder")
decoder = keras.Model(latent_inputs, decoder_outputs, name="decoder")
autoencoder = keras.Model(encoder_inputs, decoder(encoder(encoder_inputs)), name="autoencoder")


# Compile the autoencoder model using mean squared error loss and Adam optimizer
autoencoder.compile(optimizer='adam', loss='mse')


# Load MNIST dataset.  Preprocessing includes normalization to the range [0,1]
(x_train, _), (x_test, _) = keras.datasets.mnist.load_data()
x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255
x_train = np.reshape(x_train, (len(x_train), 28, 28, 1))
x_test = np.reshape(x_test, (len(x_test), 28, 28, 1))

# Train the autoencoder model
autoencoder.fit(x_train, x_train, epochs=5, batch_size=256, shuffle=True, validation_data=(x_test, x_test))


#Example of encoding and decoding an image
encoded_imgs = encoder.predict(x_test)
decoded_imgs = decoder.predict(encoded_imgs)

#The decoded images are approximations of the original images. The quality of the reconstruction depends on the complexity of the encoder/decoder and the training data
#You can visualize the original and reconstructed images to see the results.


