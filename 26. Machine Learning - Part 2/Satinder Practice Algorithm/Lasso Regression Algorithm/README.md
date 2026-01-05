# Machine Learning: From Scratch to Advanced 🚀

# Lasso Regression on Insurance Charges

This repository demonstrates a **complete end-to-end implementation of Lasso Regression** using Python and scikit-learn. The objective of the project is to **predict medical insurance charges** while applying **L1 regularization** to control model complexity and perform feature selection.

The implementation is provided in the Jupyter Notebook:

```
lasso_regression.ipynb
```

---

## 1. Project Objective

The main goals of this notebook are:

- Understand the concept of **Lasso (L1) Regularization**
- Apply Lasso Regression to a real-world dataset
- Observe the impact of regularization on model coefficients
- Reduce overfitting by penalizing large weights
- Evaluate model performance using **R² score**

---

## 2. Dataset Description

The notebook uses the **Insurance dataset** (`insurance.csv`), a commonly used dataset for regression tasks.

### Columns in the dataset:

| Column   | Description                              |
| -------- | ---------------------------------------- |
| age      | Age of the primary beneficiary           |
| sex      | Gender (male/female)                     |
| bmi      | Body Mass Index                          |
| children | Number of children covered by insurance  |
| smoker   | Smoking status (yes/no)                  |
| region   | Residential area in the US               |
| charges  | Medical insurance cost (target variable) |

---

## 3. Libraries Used

The following Python libraries are used in this project:

```python
pandas
seaborn
matplotlib
scikit-learn
```

### Purpose of each library:

- **pandas** – Data loading and manipulation
- **seaborn** – Data visualization
- **matplotlib** – Plot rendering
- **scikit-learn** – Model building, regularization, and evaluation

---

## 4. Data Loading & Exploration

The dataset is loaded using pandas:

```python
insurance_data = pd.read_csv("insurance.csv")
```

Initial exploration is done using:

- `insurance_data.head()`
- `insurance_data.shape()`
- `insurance_data.describe()`

This helps verify data integrity and understand feature distributions.

---

## 5. Data Visualization

Scatter plots are used to understand relationships between features and insurance charges.

Example:

```python
sns.scatterplot(x=insurance_data["bmi"], y=insurance_data["charges"])
```

### Observations:

- Higher BMI generally corresponds to higher insurance charges
- Smoking status significantly increases cost variability

---

## 6. Data Preprocessing & Feature Engineering

### Encoding Categorical Variables

Categorical columns such as `sex` and `smoker` are converted into numerical form to make them compatible with regression models.

### Interaction Features

To improve predictive performance, interaction features are introduced:

```python
X["age_smoker"] = X["age"] * X["smoker"]
X["bmi_smoker"] = X["bmi"] * X["smoker"]
```

These features capture the combined effect of smoking with age and BMI.

---

## 7. Feature and Target Selection

- **Features (X):** Independent variables
- **Target (y):** `charges`

```python
X = insurance_data.drop("charges", axis=1)
y = insurance_data["charges"]
```

---

## 8. Train-Test Split

The dataset is split into training and testing sets:

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

- **80% training data**
- **20% testing data**

---

## 9. Model Training – Lasso Regression

A **Lasso Regression** model is trained using scikit-learn:

```python
from sklearn.linear_model import Lasso

lasso_model = Lasso(alpha=0.01)
lasso_model.fit(X_train, y_train)
```

### Role of Alpha (α)

- Controls the strength of regularization
- Higher α → more coefficients shrink toward zero
- Helps reduce overfitting and perform feature selection

---

## 10. Model Evaluation

### R² Score

Model performance is evaluated using the **R² score** on both training and testing data.

```python
y_train_pred = lasso_model.predict(X_train)
y_test_pred = lasso_model.predict(X_test)
```

### Interpretation:

- Similar train and test R² → Good generalization
- Large performance gap → Overfitting or underfitting

---

## 11. Effect of Lasso Regularization

One of the key characteristics of Lasso Regression is **automatic feature selection**.

- Less important features may receive coefficients close to **zero**
- Important predictors retain larger weights
- Results in a simpler, more interpretable model

---

## 12. Final Observations

- Lasso Regression reduces model complexity
- Helps control overfitting compared to standard Linear Regression
- Smoking-related features remain dominant predictors
- Regularization improves model stability

---

## 13. How to Run the Notebook

1. Install dependencies:

```bash
pip install pandas seaborn matplotlib scikit-learn
```

2. Ensure `insurance.csv` is present in the same directory
3. Open the notebook:

```bash
jupyter notebook lasso_regression.ipynb
```

---

## 14. Future Improvements

- Tune alpha using cross-validation
- Compare with Ridge Regression
- Use Elastic Net
- Perform feature scaling

---

## 15. Learning Purpose

This notebook is designed for **educational purposes**, focusing on understanding **Lasso Regression and regularization** through practical implementation.

## ⭐ Contributing

Contributions are welcome!  
Feel free to open issues or submit pull requests to improve this roadmap.

---

## 📜 License

This project is licensed under the MIT License.
