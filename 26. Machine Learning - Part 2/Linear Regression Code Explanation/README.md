# Machine Learning: From Scratch to Advanced 🚀

# Linear Regression on Insurance Charges

This repository demonstrates a **complete end-to-end Linear Regression workflow** using Python and scikit-learn. The goal of the project is to **predict medical insurance charges** based on demographic and lifestyle features such as age, BMI, smoking status, etc.

The implementation is provided in a Jupyter Notebook: `LinearRegression.ipynb`.

---

## 1. Project Objective

The main objectives of this notebook are:

- Understand the fundamentals of **Linear Regression**
- Explore and visualize the dataset
- Prepare data for machine learning
- Train a Linear Regression model
- Evaluate model performance using **R² score**
- Understand **overfitting and underfitting**

---

## 2. Dataset Description

The notebook uses the **Insurance dataset** (`insurance.csv`), which is a commonly used dataset for regression problems.

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
- **scikit-learn** – Model building, training, and evaluation

---

## 4. Data Loading

The dataset is loaded using pandas:

```python
insurance_data = pd.read_csv("insurance.csv")
```

Basic inspection is performed using:

- `insurance_data.head()`
- `insurance_data.shape()`
- `insurance_data.sample()`

This helps understand the structure, size, and sample values of the dataset.

---

## 5. Data Visualization

To understand relationships between variables, scatter plots are created.

### Example:

```python
sns.scatterplot(x=insurance_data["bmi"], y=insurance_data["charges"])
```

### With categorical separation:

```python
sns.scatterplot(
    x=insurance_data["bmi"],
    y=insurance_data["charges"],
    hue=insurance_data["smoker"]
)
```

#### Insights:

- Smokers have significantly higher insurance charges
- BMI shows a positive correlation with charges

---

## 6. Data Preprocessing & Feature Engineering

### Encoding categorical variables

Categorical columns like `sex` and `smoker` are converted into numerical form so that the regression model can process them.

### Feature Engineering

New interaction features are created to improve model performance:

```python
X["age_smoker"] = X["age"] * X["smoker"]
X["bmi_smoker"] = X["bmi"] * X["smoker"]
```

These features capture the **combined effect** of age and BMI with smoking habits.

---

## 7. Feature and Target Selection

- **Features (X):** All independent variables
- **Target (y):** `charges`

```python
X = insurance_data.drop("charges", axis=1)
y = insurance_data["charges"]
```

---

## 8. Train-Test Split

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

## 9. Model Training

A Linear Regression model is created and trained:

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
```

---

## 10. Model Evaluation

### R² Score

The model performance is evaluated using the **R² (coefficient of determination)** metric.

```python
from sklearn.metrics import r2_score

y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

r2_training = r2_score(y_train, y_train_pred)
r2_testing = r2_score(y_test, y_test_pred)
```

### Interpretation:

- **High training R², high testing R²** → Good model
- **High training R², low testing R²** → Overfitting
- **Low training R², low testing R²** → Underfitting

---

## 11. Overfitting vs Underfitting Explanation

The notebook clearly explains model behavior:

- **Overfitting:** Model memorizes training data but fails to generalize
- **Underfitting:** Model fails to learn meaningful patterns

R² scores on training and testing data are used to diagnose these issues.

---

## 12. Final Observations

- Smoking status is the most influential factor in insurance charges
- Feature engineering significantly improves prediction accuracy
- Linear Regression performs reasonably well for this dataset

---

## 13. How to Run the Notebook

1. Install dependencies:

```bash
pip install pandas seaborn matplotlib scikit-learn
```

2. Ensure `insurance.csv` is in the same directory
3. Open the notebook:

```bash
jupyter notebook LinearRegression.ipynb
```

---

## 14. Future Improvements

- Try **Polynomial Regression**
- Apply **Regularization (Ridge / Lasso)**
- Compare with tree-based models
- Perform cross-validation

---

## 15. Author & Learning Purpose

This notebook is designed for educational purposes, focusing on understanding Linear Regression concepts with practical implementation.

## ⭐ Contributing

Contributions are welcome!  
Feel free to open issues or submit pull requests to improve this roadmap.

---

## 📜 License

This project is licensed under the MIT License.
