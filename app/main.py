from flask import Flask, render_template, request, jsonify
from keras.models import load_model
from PIL import Image
import numpy as np
import base64
import io

# Initialize the flask app
app = Flask(__name__)

# Load the model
model = load_model('app/model.h5')

# Handle GET requests
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# Handle POST requests
@app.route('/', methods=['POST'])
def recognize():
    # Receive base64 data from the frontend
    encoded_data = request.get_json().split(',')[1]
    
    # Decode base64 data to python array
    decoded_data = base64.urlsafe_b64decode(encoded_data)

    # Convert bytes to image
    img = Image.open(io.BytesIO(decoded_data))

    # Resize image to 28x28
    img = img.resize((28, 28))

    # Convert image to grayscale
    # NOTE: 3-channel RGB image to 1-channel grayscale image
    img = img.convert('L')

    # Convert image to numpy array
    img = np.array(img)

    # Resize image to 784
    # NOTE: The input shape of the neural network is 784
    img = img.reshape(1, 784)

    # Convert image to float32
    img = img.astype('float32')

    # Normalize the image
    img /= 255

    # Predict the digit
    prediction = model.predict(img).tolist()
    return jsonify(prediction)
