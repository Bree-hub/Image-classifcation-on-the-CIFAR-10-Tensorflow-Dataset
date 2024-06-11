# Image-classifcation-on-the-CIFAR-10-Tensorflow-Dataset
This project aims to classify images from the CIFAR-10 dataset into 10 categories: Airplane, Automobile, Bird, Cat, Deer, Dog, Frog, Horse, Ship, and Truck. The repository encompasses the complete workflow, from environment setup and exploratory data analysis to model deployment via a web application.

## Repository Structure
Image-classification-on-the-CIFAR-10-Tensorflow-Dataset/
│
├── model/                 # Directory containing trained model files
│   ├── model3.h5
│   ├── model4.h5
│   ├── model5.h5
│   ├── model6.h5
│   ├── model7.h5
│
├── test/                  # Directory for test scripts or files
│   ├── test_images.jpg
│   ├── ...
│
├── Procfile.txt           # Configuration for deploying the app (e.g., on Heroku)
├── README.md              # Project documentation (this file)
├── app.py                 # Flask web application for model inference
├── cifar_10.ipynb         # Jupyter Notebook for model training and evaluation
├── requirements.txt       # Python dependencies
└── runtime.txt            # Specifies the Python runtime environment

## Setup Instructions
Prerequisites
Python 3.7 or higher
pip (Python package installer)
