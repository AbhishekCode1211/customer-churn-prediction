# Customer Churn Prediction (ANN)

## Overview

This is Machine Learning project where I built a simple model to predict whether a customer will churn or not.
---

## Dataset

* Dataset: Credit Card Customer Churn Dataset (From Kaggle)
* Target Variable: `Exited` (0 = No Exiting, 1 = Exited)

---

## Data Preprocessing

* Removed unnecessary columns:

  * RowNumber, CustomerId, Surname
* Converted categorical variables using One-Hot Encoding:

  * Geography
  * Gender
* Feature Scaling applied using:

  * StandardScaler

---

## Model Architecture (ANN)

* Input Layer: 11 features
* Hidden Layer 1: 11 neurons (ReLU)
* Hidden Layer 2: 11 neurons (ReLU)
* Output Layer: 1 neuron (Sigmoid)

---

## Model Configuration

* Loss Function: Binary Crossentropy
* Optimizer: Adam
* Metrics: Accuracy
* Epochs: 50
* Validation Split: 20%

---

## Results

* Training Accuracy: ~86%
* Validation Accuracy: ~84%
* Model shows stable learning with no overfitting

---

## Visualization

* Plotted Training Loss vs Validation Loss
* Observed smooth convergence

---

## How to Run

1. Download the notebook
2. Install required libraries:

   ```
   pip install pandas numpy matplotlib scikit-learn tensorflow
   ```
3. Run the notebook step by step

---

## Key Learnings

* Data preprocessing and feature scaling
* Building ANN using Keras
* Binary classification using sigmoid activation
* Model evaluation using accuracy and loss graphs

---

## Author

Abhishek
