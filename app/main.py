from flask import Flask, render_template

# Initialize the flask app
app = Flask(__name__)

# Handle GET requests
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')