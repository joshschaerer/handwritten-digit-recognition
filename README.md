<p align="center">
  <a href="https://github.com/joshschaerer/handwritten-digit-recognition" rel="noopener">
 <img src="https://joshuaschaerer.ch/assets/img/handwritten-digit-recognition.png" alt="Project logo"></a>
</p>
<h3 align="center">Handwritten Digit Recognition</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/joshschaerer/handwritten-digit-recognition.svg)](https://github.com/joshschaerer/handwritten-digit-recognition/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/joshschaerer/handwritten-digit-recognition.svg)](https://github.com/joshschaerer/handwritten-digit-recognition/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE.md)

</div>

---

<p align="center">This project features a deep learning model trained on the MNIST dataset, integrated into a web-based application. It offers an interactive web interface where users can draw digits on a canvas, which are then recognized by the model in real-time.</p>

## 📝 Table of Contents

- [Problem Statement](#problem_statement)
- [Idea / Solution](#idea)
- [Dependencies / Limitations](#limitations)
- [Future Scope](#future_scope)
- [Setting up a local environment](#getting_started)
- [Usage](#usage)
- [Technology Stack](#tech_stack)
- [Contributing](#contributing)
- [Authors](#authors)
- [Acknowledgments](#acknowledgments)

## 🧐 Problem Statement <a name = "problem_statement"></a>

- **IDEAL**: Seamless digit recognition for all handwriting styles.
- **REALITY**: Varied handwriting styles lead to recognition challenges.
- **CONSEQUENCES**: Impacts data processing efficiency and user experience.

## 💡 Idea / Solution <a name = "idea"></a>

This project implements a convolutional neural network using Keras and TensorFlow, hosted on a Flask server, to improve the accuracy of recognizing handwritten digits. The interactive web application allows users to draw digits directly into a browser, which the model then evaluates in real-time.

## ⛓️ Dependencies / Limitations <a name = "limitations"></a>

- **Dependencies**: Python, Flask, TensorFlow, Keras, PIL, NumPy.
- **Limitations**: Performance can degrade with unusual handwriting or poor image quality.
- **Impact**: While effective, these limitations suggest room for further model training and refinement.

## 🚀 Future Scope <a name = "future_scope"></a>

Potential future developments include enhancing the model to improve the accuracy of recognizing single digits and extending the model's capabilities to recognize sequences of multiple digits, which would significantly broaden its practical applications.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will help you set up and run the project locally.

### Prerequisites

Install the required Python packages:

```bash
pip install flask tensorflow keras pillow numpy
```

### Installing

Clone the repository and navigate to it:

```bash
git clone https://github.com/joshschaerer/handwritten-digit-recognition.git
cd handwritten-digit-recognition
```

Run the Flask application:

```bash
flask run
```

## 🎈 Usage <a name="usage"></a>

After starting the server, navigate to `http://127.0.0.1:5000` in your web browser. Use the drawing canvas to draw a digit with your mouse or touchscreen. The application will display the recognized digit and its confidence score.

## ⛏️ Built With <a name = "tech_stack"></a>

- [Flask](https://flask.palletsprojects.com/) - Web Framework
- [TensorFlow](https://www.tensorflow.org/) - ML Framework
- [Keras](https://keras.io/) - Neural Network API
- [PIL](https://python-pillow.org/) - Python Imaging Library
- [NumPy](https://numpy.org/) - Numerical Processing

## ✏️ Contributing <a name = "contributing"></a>

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

## 👋 Authors <a name = "authors"></a>

- [@joshschaerer](https://github.com/joshschaerer) - Initial Work

See also the list of [contributors](https://github.com/joshschaerer/handwritten-digit-recognition/contributors) who participated in this project.

## 🎉 Acknowledgments <a name = "acknowledgments"></a>

- Thanks to those who contributed to TensorFlow and Keras, without which this project wouldn't be possible.
- Inspired by the ongoing advancements in machine learning and computer vision.

## 📜 License

Copyright © 2024 Joshua Schärer.  
This project is licensed under the terms of the [MIT](LICENSE.md) license.
