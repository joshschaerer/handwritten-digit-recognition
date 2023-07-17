"""
1st Model: Single Layer Perceptron
----------------------------------
This model is the most basic sequential model with 0 hidden layers in it.
Test accuracy: 0.92
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

# Define the architecture of the model
model_1 = Sequential()

# Add layers to the model
    # Input layer with 784 neurons
    # Output layer with 10 neurons
model_1.add(Dense(10,input_shape=(784,),name='dense_layer', activation='softmax')) 

# Compiling the model
model_1.compile(optimizer='SGD', 
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Training the model.
training = model_1.fit(x_train, y_train, batch_size=64, epochs=70, validation_split=0.2) 

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
test_loss, test_acc = model_1.evaluate(x_test, y_test)
print('Test accuracy:', test_acc)