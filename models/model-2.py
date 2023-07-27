"""
2nd Model: Multi Layer Perceptron
----------------------------------
This model includes 1 hidden layer and 3 dense layers.
Test accuracy: 0.97
"""

# Import all libraries
    # TensorFlow
    # Matplotlib
    # Dataset
import tensorflow as tf
from tensorflow.keras.layers import Dense
from tensorflow.keras import Sequential
import matplotlib.pyplot as plt
from dataset import x_train, y_train, x_test, y_test

# Define the architecture of the model
model_2 = Sequential()
N_HIDDEN = 64

# Add layers to the model
    # Input layer with 784 neurons
    # Hidden layer with 64 neurons
    # Output layer with 10 neurons
model_2.add(Dense(N_HIDDEN, input_shape=(784,), name="dense_layer", activation='relu')) # Input: 784 Neurons, Output: 64 Neurons
model_2.add(Dense(N_HIDDEN, name="dense_layer_2", activation='relu')) # Input: 64 Neurons, Output: 64 Neurons
model_2.add(Dense(10, name="dense_layer_3", activation='softmax')) # Input: 64 Neurons, Output: 10 Neurons

# Compiling the model
model_2.compile(optimizer='SGD',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

# Training the model
training = model_2.fit(x_train, y_train, batch_size=64, epochs=100, validation_split=0.2)

# Print data in training
print(training.history.keys())

# Plot the training for accuracy
plt.plot(training.history['accuracy'])
plt.plot(training.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

# Plot the training for loss
plt.plot(training.history['loss'])
plt.plot(training.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

# Evaluate the model
test_loss, test_acc = model_2.evaluate(x_test, y_test)
print('Test accuracy:', test_acc)

# Save the model
model_2.save('app/model.h5')