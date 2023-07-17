
"""
Handwritten Digit Recognition dataset
"""

# Import all libraries
    # TensorFlow
    # Keras
import tensorflow as tf
from tensorflow import keras 

# Load the dataset
mnist = keras.datasets.mnist

# Split the dataset into training and testing
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Prepare the dataset
# NOTE: The data is reshaped from 28x28 to 784
#       because the input layer of the neural
#       network has 784 neurons
RESHAPED = 784 # 28x28 = 784 neurons
x_train = x_train.reshape(60000, RESHAPED)
x_test = x_test.reshape(10000, RESHAPED)

# Convert the data
# NOTE: The data is converted to float32 to use 32-bit
#       precision; this will help in training
#       neural networks faster
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

# Normalize the data
# NOTE: The data is normalized to the maximum
#       intensity value. In this case, the
#       maximum value is 255
x_train /= 255
x_test /= 255

print(x_train.shape[0], 'train samples') 
print(x_test.shape[0], 'test samples') 

# One-hot representation of the labels.
y_train = tf.keras.utils.to_categorical(y_train, 10) 
y_test = tf.keras.utils.to_categorical(y_test, 10)
