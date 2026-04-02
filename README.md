# Phishing Website Detection using Deep Learning (CNN)

A deep learning-based system for detecting phishing websites using **URL analysis** and **Convolutional Neural Networks (CNN)**.
This project aims to classify URLs as **phishing** or **legitimate** with high accuracy.

---

## Overview

Phishing attacks are a major cybersecurity threat where attackers create fake websites to steal sensitive information. Traditional detection methods fail to identify new phishing URLs.

This project uses **Deep Learning (CNN)** to automatically learn patterns from URL structures and detect phishing websites effectively.

---

##  Features

* URL-based phishing detection
* CNN model for automatic feature extraction
* Character-level embedding for URL processing
* Performance evaluation using standard metrics
* High accuracy and generalization capability

---

##  Dataset

* Source: **PhishTank Dataset**
* Total URLs: ~55,000
* Classes:

  * Phishing (1)
  * Legitimate (0)

---

## 🧠 Model Architecture

The model is based on a **1D Convolutional Neural Network (CNN)**:

* Conv1D Layer
* Batch Normalization
* Dropout Layers
* Flatten Layer
* Dense Layer
* Output Layer (Binary Classification)

---

## Workflow

```
URL Input → Preprocessing → Character Embedding → CNN Model → Prediction
```

---

## Performance Metrics

The model is evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* AUC-ROC

---

## Results

* High training and validation accuracy
* Strong generalization on unseen data
* Effective detection of phishing URLs

---

## Tech Stack

* Python
* TensorFlow / Keras
* NumPy, Pandas
* Scikit-learn
* Matplotlib / Seaborn

---

## Project Structure

```
├── data/        # Dataset files
├── src/         # Model training and preprocessing code
├── models/      # Saved trained models
├── requirements.txt   # Required libraries to run code 
└── README.md
```

---

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/Harshit-Maurya838/PhishDetect
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Notebook:

```bash
python 03_train_model.ipynb
```
*Run all cells sequentially from top to bottom
This will:

*Load and preprocess the dataset
*Perform feature extraction and encoding
*Train the CNN model
*Generate performance graphs (accuracy, loss, etc.)
*Evaluate the model
---

## Applications

* Web browser security
* Email phishing detection
* Banking and financial fraud prevention
* Cybersecurity tools

---

## Future Work

* CNN + LSTM hybrid models
* Real-time deployment (API / browser extension)
* Explainable AI integration
* Faster prediction optimization

---

## References

* Aldakheel et al., *Deep Learning-Based Phishing Detection*, 2023
* PhishTank Dataset: https://www.phishtank.com

---

## Contributors

* Harsh Panchal
* Naman Chaudhary
* Harshit Maurya
* Nishtha Maurya
* Shiv Gaikwad

---
