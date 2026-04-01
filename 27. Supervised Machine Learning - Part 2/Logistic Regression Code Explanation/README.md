# Machine Learning: From Scratch to Advanced 🚀

# Logistic Regression on Heart Disease Dataset

This repository demonstrates a **complete end-to-end implementation of Logistic Regression** using Python and scikit-learn. The goal of this project is to **predict the presence of heart disease** using patient health attributes, framing the problem as a **binary classification task**.

The implementation is provided in the Jupyter Notebook:

```
logistic_regression.ipynb
```

---

## 1. Project Objective

The main objectives of this notebook are:

- Understand the fundamentals of **Logistic Regression**
- Apply Logistic Regression to a **classification problem**
- Learn how features influence binary outcomes
- Train and evaluate a classification model
- Measure model performance using **accuracy and precision**

---

## 2. Dataset Description

The notebook uses the **Heart Disease dataset** (`heart.csv`), which is commonly used for binary classification tasks in machine learning.

### Columns in the dataset:

| Column   | Description                              |
| -------- | ---------------------------------------- |
| age      | Age of the patient                       |
| sex      | Gender (1 = male, 0 = female)            |
| cp       | Chest pain type                          |
| trestbps | Resting blood pressure                   |
| chol     | Serum cholesterol                        |
| fbs      | Fasting blood sugar                      |
| restecg  | Resting ECG results                      |
| thalach  | Maximum heart rate achieved              |
| exang    | Exercise induced angina                  |
| oldpeak  | ST depression induced by exercise        |
| slope    | Slope of the peak exercise ST segment    |
| ca       | Number of major vessels                  |
| thal     | Thalassemia                              |
| target   | Heart disease presence (1 = yes, 0 = no) |

---

## 3. Libraries Used

The following Python libraries are used in this project:

```python
pandas
seaborn
scikit-learn
```

### Purpose of each library:

- **pandas** – Data loading and manipulation
- **seaborn** – Data exploration
- **scikit-learn** – Model training and evaluation

---

## 4. Data Loading

The dataset is loaded using pandas:

```python
heart_df = pd.read_csv("heart.csv")
```

Initial inspection is performed using:

- `heart_df.head()`
- `heart_df.shape()`
- `heart_df.info()`

This helps verify the structure and data types of the dataset.

---

## 5. Feature and Target Selection

- **Features (X):** All columns except the target
- **Target (y):** `target`

```python
X = heart_df.drop("target", axis=1)
y = heart_df["target"]
```

---

## 6. Train-Test Split

The dataset is split into training and testing sets:

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

- **80% training data**
- **20% testing data**

---

## 7. Model Training

A Logistic Regression model is created and trained:

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
```

The model learns the relationship between health indicators and the probability of heart disease.

---

## 8. Model Evaluation

The model is evaluated using classification metrics:

```python
from sklearn.metrics import accuracy_score, precision_score
```

### Metrics Used

- **Accuracy:** Overall correctness of predictions
- **Precision:** Proportion of correctly predicted positive cases

These metrics help assess how reliably the model predicts heart disease.

---

## 9. Final Observations

- Logistic Regression performs well for binary classification problems
- Health-related features show meaningful influence on predictions
- Accuracy and precision provide clear insight into model performance
- Logistic Regression is simple, interpretable, and effective

---

## 10. How to Run the Notebook

1. Install dependencies:

```bash
pip install pandas seaborn scikit-learn
```

2. Ensure `heart.csv` is in the same directory
3. Open the notebook:

```bash
jupyter notebook logistic_regression.ipynb
```

---

## 11. Future Improvements

- Feature scaling
- Add recall and F1-score
- Hyperparameter tuning
- Compare with other classifiers (KNN, Decision Trees)

---

## 12. Learning Purpose

This notebook is designed for **educational purposes**, focusing on understanding **Logistic Regression for binary classification** using a real-world medical dataset.

## ⭐ Contributing

Contributions are welcome!  
Feel free to open issues or submit pull requests to improve this roadmap.

---

## 📜 License

This project is licensed under the MIT License.
