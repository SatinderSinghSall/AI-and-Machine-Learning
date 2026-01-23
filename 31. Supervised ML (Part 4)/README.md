# Machine Learning: From Scratch to Advanced 🚀

# 🌳 Decision Tree Algorithms (Supervised Machine Learning)

## 📌 Classification & Regression using Decision Trees (End-to-End Workflow)

This repository contains two complete Machine Learning projects based on **Decision Tree Algorithms**, implemented using real datasets with a focus on:

✅ Data understanding & preprocessing  
✅ Building supervised ML models  
✅ Training & testing workflow  
✅ Model evaluation & interpretation  
✅ Understanding how Decision Trees work (not treating ML as a black box)

---

## 📂 Project Files Included

| Notebook                              | Algorithm Type           | Problem Type   | Dataset                      |
| ------------------------------------- | ------------------------ | -------------- | ---------------------------- |
| `decision-tree-algo-classifier.ipynb` | Decision Tree Classifier | Classification | Titanic Dataset (`seaborn`)  |
| `decision-tree-algo-regressor.ipynb`  | Decision Tree Regressor  | Regression     | Diabetes Dataset (`sklearn`) |

---

# 🧠 What is a Decision Tree?

A **Decision Tree** is a supervised learning algorithm that works by repeatedly splitting the dataset into smaller groups based on feature conditions, forming a tree-like structure.

It is widely used because it is:

✅ Easy to understand  
✅ Interpretable (can visualize the tree)  
✅ Works with both numerical & categorical data  
✅ Can solve both classification and regression problems

---

# 🌳 How Decision Trees Work (Core Idea)

A Decision Tree learns rules in the form:

> If (feature condition is true) → go left  
> Else → go right

Each split is chosen based on how well it separates the data.

### 🔹 For Classification:

The goal is to split data so that each leaf contains mostly one class (pure nodes).

Common splitting criteria:

- **Gini Impurity**
- **Entropy (Information Gain)**

### 🔹 For Regression:

The goal is to split data so that the target values in each leaf are as close as possible.

Common splitting criteria:

- **Mean Squared Error (MSE)**
- **Variance reduction**

---

# ✅ 1. Decision Tree Classifier Notebook

📌 `decision-tree-algo-classifier.ipynb`

## 🔍 Problem Statement

Build a **classification model** to predict whether a passenger survived the Titanic disaster.

### 🎯 Target Variable

- `survived`
  - `0` → Did not survive
  - `1` → Survived

### 📌 Dataset Used

- Titanic dataset loaded using:

```python
sns.load_dataset("titanic")
```

---

## 🛠️ Workflow Implemented

### 1️⃣ Data Loading

- Loaded Titanic dataset
- Previewed dataset using `.head()`

### 2️⃣ Data Understanding (EDA Basics)

- Checked dataset columns, structure
- Identified missing values
- Selected relevant features

### 3️⃣ Data Preprocessing

Decision Trees require **numerical input**, so categorical features must be encoded.

Preprocessing steps included:

- Handling missing values (dropping/filling)
- Feature selection
- Encoding categorical variables into numeric form
- Train-test splitting

---

## 🧪 Model Training

Model used:

```python
DecisionTreeClassifier()
```

The model learns splitting rules to classify passengers into:
✅ Survived
❌ Not Survived

---

## 📊 Evaluation Metrics Used

The notebook evaluates performance using:

### ✅ Accuracy Score

Accuracy tells the percentage of correct predictions:

```python
accuracy_score(y_test, y_pred)
```

### ✅ Confusion Matrix (Recommended)

A confusion matrix helps understand true/false predictions:

- True Positive
- True Negative
- False Positive
- False Negative

### ✅ Precision / Recall / F1-score (Recommended)

For better evaluation, classification models should also be checked with:

- Precision → How many predicted survivors actually survived?
- Recall → How many actual survivors were correctly found?
- F1-score → Balance between precision & recall

---

## 🌳 Tree Visualization

The notebook visualizes the Decision Tree using:

```python
plot_tree(model, filled=True)
```

This helps interpret:

- Feature splits
- Decision rules
- Leaf node outcomes

---

## ✅ Key Learnings (Classifier)

✔ How Decision Trees classify data using splitting rules
✔ How feature selection affects model performance
✔ Why encoding categorical features is important
✔ How to evaluate classification models using accuracy
✔ How to interpret a Decision Tree visually

---

---

# ✅ 2. Decision Tree Regressor Notebook

📌 `decision-tree-algo-regressor.ipynb`

## 🔍 Problem Statement

Build a **regression model** to predict a continuous target value using the Diabetes dataset.

### 🎯 Target Variable

- `target` → a numeric value representing disease progression

### 📌 Dataset Used

Diabetes dataset loaded using:

```python
load_diabetes(as_frame=True)
```

---

## 🛠️ Workflow Implemented

### 1️⃣ Data Loading

- Loaded Diabetes dataset into a DataFrame
- Checked dataset shape and previewed data

### 2️⃣ Feature & Target Split

```python
X = df.drop("target", axis=1)
y = df["target"]
```

### 3️⃣ Train-Test Split

Split data into:

- Training set → used for learning patterns
- Testing set → used for evaluation

---

## 🧪 Model Training

Model used:

```python
DecisionTreeRegressor()
```

This model predicts numeric values by learning splitting rules that reduce error.

---

## 📊 Evaluation Metrics Used

### ✅ R² Score (Coefficient of Determination)

Measures how well the model explains variance:

- `1.0` → perfect prediction
- `0.0` → no improvement over mean baseline
- `<0` → worse than baseline

```python
r2_score(y_test, y_pred)
```

### ✅ Mean Squared Error (MSE)

Measures average squared prediction error:

```python
mean_squared_error(y_test, y_pred)
```

### ✅ RMSE (Recommended)

RMSE is the square root of MSE and is easier to interpret:

```python
mean_squared_error(y_test, y_pred, squared=False)
```

---

## 🌳 Tree Visualization

Decision tree plotted using:

```python
plot_tree(regressor, filled=True)
```

This helps understand:

- Which features influence predictions
- How splits are made
- Leaf node prediction values

---

## ✅ Key Learnings (Regressor)

✔ How Decision Trees handle regression problems
✔ How splitting reduces error in continuous prediction
✔ Why overfitting is common in deep trees
✔ How to evaluate regression models using R² and MSE
✔ Visual interpretation of regression tree structure

---

# ⚠️ Important Concepts: Overfitting in Decision Trees

Decision Trees can easily **overfit** when they grow too deep.

### Signs of Overfitting:

- Very high training score
- Low test score

### How to Control Overfitting:

Use hyperparameters such as:

- `max_depth`
- `min_samples_split`
- `min_samples_leaf`
- `max_features`

Example:

```python
DecisionTreeClassifier(max_depth=4, min_samples_leaf=5, random_state=42)
```

---

# 📌 Requirements (Dependencies)

Install required libraries:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```

---

# ▶️ How to Run the Notebooks

1. Clone the repository
2. Open Jupyter Notebook / Jupyter Lab
3. Run each notebook cell-by-cell

```bash
jupyter notebook
```

---

# 📈 Next Improvements (Planned Enhancements)

🚀 Future enhancements that can be added:

✅ Add `classification_report` & confusion matrix for classifier
✅ Add `RMSE` metric for regressor
✅ Compare train vs test score to detect overfitting
✅ Hyperparameter tuning using GridSearchCV
✅ Feature importance visualization
✅ Cross-validation for more reliable results
✅ Build a reusable ML pipeline structure

---

# 🧑‍💻 Author

**Satinder Singh**
Machine Learning Learner | AI & Data Science Enthusiast
📌 Focused on learning by building end-to-end ML projects.

---

# ⭐ If you found this helpful

Feel free to ⭐ the repository and share feedback or suggestions for improvements!
