# Iris Flower Classification with Logistic Regression

This project demonstrates my first Machine Learning model, built during the **Oracle Cloud Infrastructure AI Foundations** course, to classify iris flowers based on their sepal and petal measurements.

## Dataset
The [Iris dataset](https://archive.ics.uci.edu/ml/datasets/iris) contains 150 samples of iris flowers with the following features:
- Sepal Length (cm)
- Sepal Width (cm)
- Petal Length (cm)
- Petal Width (cm)

## How It Works
1. Load the dataset
2. Preprocess data into features (X) and labels (y)
3. Train a Logistic Regression model
4. Make predictions

## Running the Project
```bash
# Clone the repository
git clone https://github.com/yourusername/iris-ml-project.git
cd iris-ml-project

# Install dependencies
pip install -r requirements.txt

# Example Output
First 5 rows of the dataset:
   Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm     Species
0   1           5.1           3.5            1.4           0.2  Iris-setosa
...

Prediction for [[4.6, 3.5, 1.5, 0.2]]: Iris-setosa


# Run the script
python iris_model.py
