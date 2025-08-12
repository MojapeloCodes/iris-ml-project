# iris_model.py
"""
Iris Flower Classification using Logistic Regression
Author: Tshepiso
Description: This script trains a logistic regression model to classify iris species based on sepal and petal measurements.
"""

# 1. Import the necessary libraries
import pandas as pd
from sklearn.linear_model import LogisticRegression

# 2. Load the dataset and view the first 5 rows
iris_data = pd.read_csv("Iris.csv")
print("First 5 rows of the dataset:")
print(iris_data.head())

# 3. Split the data into features (X) and labels (Y)
X = iris_data.drop(columns=["Id", "Species"])  # Features
Y = iris_data["Species"]                       # Labels

# 4. Create a logistic regression model
model = LogisticRegression(max_iter=200)  # Increase iterations for convergence

# 5. Train the model
model.fit(X.values, Y)

# 6. Make a prediction for a new sample
sample_data = [[4.6, 3.5, 1.5, 0.2]]  # Sepal length, Sepal width, Petal length, Petal width
prediction = model.predict(sample_data)

# 7. Print the prediction
print(f"Prediction for {sample_data}: {prediction[0]}")
