# Machine Learning Algorithms – Detailed Walkthrough

This repository contains **three Jupyter notebooks** demonstrating core machine learning algorithms using **scikit-learn**. Each notebook focuses on a different model family and includes data loading, preprocessing, model training, evaluation, and experimentation with hyperparameters.

The goal of these notebooks is to build **conceptual clarity + practical intuition** around tree-based models and Support Vector Machines (SVMs) for both **classification and regression** problems.

---

## 1. Random Forest & Ensemble Learning
**Notebook:** `random-forest.ipynb`

### Objective
To understand **tree-based models** and how ensemble techniques like **Random Forest** and **Bagging** improve performance and generalization.

### Dataset
- **Titanic dataset** (loaded via `seaborn.load_dataset`)
- Target: `survived`
- Features used:
  - `pclass`
  - `sex`
  - `fare`
  - `embarked`

### Data Preprocessing
- Categorical variables (`sex`, `embarked`) are encoded
- Missing values handled implicitly by dataset cleaning
- Data split into **training and testing sets**

### Models Implemented

#### 1. Decision Tree Classifier
- Used as a **baseline model**
- `max_depth=4` to control overfitting
- Decision tree visualization included using `plot_tree`

**Key Concepts:**
- Information Gain / Gini Impurity
- Overfitting in deep trees
- Interpretability of decision trees

---

#### 2. Random Forest Classifier
- Ensemble of **multiple decision trees**
- Parameters:
  - `n_estimators = 501`
  - Bootstrapped sampling
  - Feature randomness at each split

**Why Random Forest?**
- Reduces variance
- More robust than a single decision tree
- Works well on tabular data

---

#### 3. Bagging Classifier
Two base estimators are explored:

1. **Decision Tree as base model**
2. **Logistic Regression as base model**

**Bagging (Bootstrap Aggregating):**
- Trains multiple models on random subsets of data
- Reduces variance
- Improves stability

---

### Key Takeaways
- Decision Trees are easy to interpret but prone to overfitting
- Random Forest significantly improves accuracy and stability
- Bagging generalizes the idea of ensemble learning beyond trees

---

## 2. Support Vector Machine – Classification
**Notebook:** `svm-c-imp.ipynb`

### Objective
To understand **Support Vector Machines for classification**, kernel functions, and the impact of the **C hyperparameter**.

### Dataset
- **Iris dataset** (`sklearn.datasets.load_iris`)
- Target: flower species (3 classes)

### Data Preprocessing
- Features separated into `X`, labels into `y`
- Train-test split applied
- **Standardization using `StandardScaler`** (very important for SVMs)

---

### Model Implementation

#### 1. Default SVC
- Kernel: RBF (default)
- Trained on scaled data
- Accuracy evaluated using:
  - Accuracy Score
  - Classification Report

---

#### 2. Kernel Experiments
Different kernels are explored:

- **Linear Kernel** – for linearly separable data
- **Polynomial Kernel** – captures polynomial relationships
- **Sigmoid Kernel** – behaves like a neural network activation

This demonstrates how kernel choice affects decision boundaries.

---

#### 3. Hyperparameter Tuning – C Parameter

- `C` controls the **regularization strength**
- Tested values: `[0.5, 1, 2, 3, 4, 5]`

**Conceptual Insight:**
- Low `C` → wider margin, more bias
- High `C` → narrow margin, more variance

---

### Key Takeaways
- Feature scaling is mandatory for SVMs
- Kernel choice defines model flexibility
- `C` balances margin width vs misclassification

---

## 3. Support Vector Machine – Regression (SVR)
**Notebook:** `svm-r-imp.ipynb.ipynb`

### Objective
To apply **Support Vector Regression (SVR)** on a continuous target and understand kernel effects and hyperparameter tuning.

### Dataset
- **Diabetes dataset** (`sklearn.datasets.load_diabetes`)
- Target: disease progression measure

---

### Data Preprocessing
- Features split into `X`, target into `y`
- Train-test split
- Target variable scaled using `StandardScaler`

> Scaling the target is important for SVR to stabilize optimization

---

### Model Implementation

#### 1. Default SVR
- Kernel: RBF
- Model trained on training data
- Evaluation using:
  - R² Score (Train & Test)

---

#### 2. Kernel Experiments

The following kernels are tested:
- Linear
- Polynomial
- Sigmoid

This helps compare linear vs non-linear regression performance.

---

### Hyperparameter Tuning – GridSearchCV

Parameters explored:
```text
C: [1, 2, 5, 10, 50, 100]
Kernel: [rbf, linear]
```

- Best parameters identified using cross-validation
- Best model retrained and evaluated

---

### LinearSVR
- Faster alternative for linear regression problems
- Suitable for large datasets
- Compared against kernel-based SVR

---

### Key Takeaways
- SVR is powerful for non-linear regression
- Scaling both features and target improves results
- GridSearchCV is essential for optimal performance

---

## Overall Learning Outcomes

By completing these three notebooks, you have learned:

- Tree-based learning and ensemble methods
- SVMs for classification and regression
- Kernel trick and margin maximization
- Importance of scaling in distance-based models
- Hyperparameter tuning using GridSearchCV

---

## Recommended Next Steps
- Add **cross-validation** to all models
- Compare with **XGBoost / Gradient Boosting**
- Visualize **decision boundaries** for SVM classification
- Apply models to a real-world dataset

---

✅ This README is designed to be **interview-ready, beginner-friendly, and concept-focused** while staying close to the actual notebook implementations.

