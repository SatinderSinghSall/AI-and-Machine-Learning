# Ensemble Learning Algorithms – Detailed Overview

This repository demonstrates **six popular ensemble machine learning algorithms**, each implemented in a separate Jupyter Notebook using **scikit-learn** (and **XGBoost** where applicable). The notebooks focus on **synthetic datasets**, clean workflows, and clear demonstrations of how each algorithm works internally and practically.

---

## 📂 Files Overview

| File Name                            | Algorithm                                            |
| ------------------------------------ | ---------------------------------------------------- |
| `ada-boost.ipynb`                    | AdaBoost (Adaptive Boosting) – Classification        |
| `gradient-boosting-classifier.ipynb` | Gradient Boosting – Classification                   |
| `gradient-boosting-regressor-.ipynb` | Gradient Boosting – Regression                       |
| `stacking-algorithm.ipynb`           | Stacking Ensemble – Classification & Regression      |
| `voting-algorithm.ipynb`             | Voting Ensemble – Classification & Regression        |
| `xg-boost-algo.ipynb`                | Extreme Gradient Boosting (XGBoost) – Classification |

---

## 1️⃣ AdaBoost Algorithm (`ada-boost.ipynb`)

### 🔍 Algorithm Concept

**AdaBoost (Adaptive Boosting)** builds a strong classifier by combining multiple **weak learners** (typically decision stumps). Each subsequent model focuses more on the samples that previous models misclassified.

### 🧠 How It Works

1. Initialize equal weights for all samples
2. Train a weak learner (decision tree stump)
3. Increase weights of misclassified samples
4. Train the next learner on weighted data
5. Combine learners using weighted voting

### 🛠 Implementation Details

- Dataset: `make_classification`
- Base estimator: `DecisionTreeClassifier(max_depth=1)`
- Ensemble model: `AdaBoostClassifier`
- Key parameters:
  - `n_estimators=200`
  - `random_state=42`

### 📊 Evaluation

- Accuracy Score
- Classification Report

---

## 2️⃣ Gradient Boosting Classifier (`gradient-boosting-classifier.ipynb`)

### 🔍 Algorithm Concept

Gradient Boosting builds models **sequentially**, where each new model learns to correct the **residual errors** of the previous ensemble using gradient descent optimization.

### 🧠 How It Works

1. Train an initial weak model
2. Compute residual errors
3. Train next model on residuals
4. Update ensemble predictions
5. Repeat for multiple iterations

### 🛠 Implementation Details

- Dataset: `make_classification`
- Model: `GradientBoostingClassifier`
- Key parameters:
  - `n_estimators=150`
  - `learning_rate=0.1`
  - `max_depth=3`

### 📊 Evaluation

- Accuracy Score

---

## 3️⃣ Gradient Boosting Regressor (`gradient-boosting-regressor-.ipynb`)

### 🔍 Algorithm Concept

The regression version of Gradient Boosting predicts **continuous values** by minimizing a loss function (typically squared error) using gradient descent.

### 🧠 How It Works

- Same boosting principle as classification
- Trees are trained to predict residual errors
- Ensemble output is the sum of all tree predictions

### 🛠 Implementation Details

- Dataset: `make_regression`
- Model: `GradientBoostingRegressor`
- Key parameters:
  - `n_estimators=200`
  - `learning_rate=0.05`
  - `max_depth=3`
  - `subsample=0.8`

### 📊 Evaluation

- R² Score

---

## 4️⃣ Stacking Ensemble Algorithm (`stacking-algorithm.ipynb`)

### 🔍 Algorithm Concept

**Stacking** combines multiple diverse models and trains a **meta-model** on their predictions to improve overall performance.

### 🧠 How It Works

1. Train multiple base learners
2. Generate predictions from base models
3. Use predictions as features
4. Train a final meta-learner

### 🛠 Implementation Details

#### Classification

- Base models:
  - Logistic Regression
  - Support Vector Classifier
  - Decision Tree Classifier
- Meta-model: Logistic Regression

#### Regression

- Base models:
  - Linear Regression
  - Decision Tree Regressor
  - Support Vector Regressor
- Meta-model: Linear Regression

### 📊 Evaluation

- Accuracy Score (Classification)
- R² Score (Regression)

---

## 5️⃣ Voting Ensemble Algorithm (`voting-algorithm.ipynb`)

### 🔍 Algorithm Concept

Voting ensembles combine predictions from multiple models using **majority voting (classification)** or **averaging (regression)**.

### 🧠 How It Works

- Train multiple independent models
- Aggregate predictions:
  - Hard voting → majority class
  - Soft voting → average probabilities

### 🛠 Implementation Details

#### Classification

- Models:
  - Logistic Regression
  - Support Vector Classifier
  - Decision Tree Classifier
- Model: `VotingClassifier`

#### Regression

- Models:
  - Linear Regression
  - Support Vector Regressor
  - Decision Tree Regressor
- Model: `VotingRegressor`

### 📊 Evaluation

- Accuracy Score
- R² Score

---

## 6️⃣ XGBoost Algorithm (`xg-boost-algo.ipynb`)

### 🔍 Algorithm Concept

**XGBoost (Extreme Gradient Boosting)** is an optimized, regularized version of gradient boosting designed for high performance and scalability.

### 🧠 Key Enhancements

- Regularization (L1 & L2)
- Parallel tree construction
- Efficient handling of missing values
- Tree pruning and optimized loss functions

### 🛠 Implementation Details

- Library: `xgboost`
- Dataset: `make_classification`
- Model: `XGBClassifier`
- Key parameters:
  - `n_estimators=100`
  - `max_depth=3`
  - `learning_rate=0.1`
  - `eval_metric='logloss'`

### 📊 Evaluation

- Accuracy Score
- Classification Report

---

## ✅ Summary

These notebooks collectively demonstrate how **ensemble learning** improves predictive performance by combining multiple models. The progression from **simple voting** to **advanced boosting techniques** (AdaBoost, Gradient Boosting, XGBoost) provides a strong conceptual and practical foundation for ensemble methods in machine learning.

---

📌 **Tech Stack:** Python, scikit-learn, XGBoost, NumPy

📘 Ideal for learning, interviews, and academic projects

# Ensemble Learning Algorithms - Part 2

## Interview • Academic • Production-Ready Documentation

This repository presents **six core ensemble learning algorithms**, implemented in Python using **scikit-learn** and **XGBoost**. The project is designed to serve **three audiences simultaneously**:

- 🎓 **Academic**: Clear algorithmic intuition and methodological structure
- 💼 **Interview**: Concise explanations, assumptions, and trade-offs
- 🚀 **Production**: Clean workflows, reproducibility, and evaluation practices

Each notebook demonstrates a complete machine learning pipeline: **data generation → model training → prediction → evaluation**.

---

## Repository Structure

| File                                 | Algorithm                           | Task Type                   |
| ------------------------------------ | ----------------------------------- | --------------------------- |
| `ada-boost.ipynb`                    | AdaBoost (Adaptive Boosting)        | Classification              |
| `gradient-boosting-classifier.ipynb` | Gradient Boosting                   | Classification              |
| `gradient-boosting-regressor-.ipynb` | Gradient Boosting                   | Regression                  |
| `stacking-algorithm.ipynb`           | Stacking Ensemble                   | Classification & Regression |
| `voting-algorithm.ipynb`             | Voting Ensemble                     | Classification & Regression |
| `xg-boost-algo.ipynb`                | XGBoost (Extreme Gradient Boosting) | Classification              |

---

## 1. AdaBoost (Adaptive Boosting)

**File:** `ada-boost.ipynb`

### Problem Addressed

Single weak learners often underfit complex patterns. AdaBoost converts multiple weak learners into a strong classifier by **iteratively focusing on hard-to-classify samples**.

### Algorithm Intuition (Interview-Ready)

- Weak learners are trained sequentially
- Misclassified samples receive higher weights
- Later models prioritize these difficult samples
- Final prediction is a weighted vote of all learners

### Algorithm Steps (Academic)

1. Initialize uniform sample weights
2. Train a weak learner (decision stump)
3. Increase weights for misclassified points
4. Repeat for _N_ estimators
5. Aggregate predictions using weighted voting

### Implementation Details (Production)

- Base model: `DecisionTreeClassifier(max_depth=1)`
- Ensemble: `AdaBoostClassifier`
- Key hyperparameters:
  - `n_estimators=200`
  - `random_state=42`

### Evaluation Metrics

- Accuracy
- Classification Report

---

## 2. Gradient Boosting Classifier

**File:** `gradient-boosting-classifier.ipynb`

### Problem Addressed

Instead of reweighting data (AdaBoost), Gradient Boosting **optimizes a loss function directly** using gradient descent in function space.

### Algorithm Intuition (Interview-Ready)

- Models are added sequentially
- Each model learns from the **residual errors** of the previous ensemble
- Small learning steps reduce overfitting

### Algorithm Steps (Academic)

1. Initialize with a constant model
2. Compute negative gradient (residuals)
3. Train a decision tree on residuals
4. Update ensemble prediction
5. Repeat for _N_ iterations

### Implementation Details (Production)

- Model: `GradientBoostingClassifier`
- Hyperparameters:
  - `n_estimators=150`
  - `learning_rate=0.1`
  - `max_depth=3`

### Evaluation Metrics

- Accuracy Score

---

## 3. Gradient Boosting Regressor

**File:** `gradient-boosting-regressor-.ipynb`

### Problem Addressed

Predicting continuous values while minimizing regression loss using an additive ensemble of trees.

### Key Differences from Classification

- Optimizes **Mean Squared Error (MSE)** by default
- Outputs continuous predictions

### Algorithm Intuition (Interview-Ready)

Each tree predicts **how much the current prediction is wrong**, and corrections are added gradually.

### Implementation Details (Production)

- Model: `GradientBoostingRegressor`
- Hyperparameters:
  - `n_estimators=200`
  - `learning_rate=0.05`
  - `max_depth=3`
  - `subsample=0.8`

### Evaluation Metrics

- R² Score

---

## 4. Stacking Ensemble

**File:** `stacking-algorithm.ipynb`

### Problem Addressed

No single model performs best across all data distributions. Stacking learns **how to combine models optimally**.

### Algorithm Intuition (Interview-Ready)

- Base models capture different patterns
- Meta-model learns which base model to trust

### Algorithm Steps (Academic)

1. Train multiple base learners
2. Generate out-of-fold predictions
3. Use predictions as features
4. Train a meta-learner

### Implementation Details (Production)

**Classification Stack**

- Base models: Logistic Regression, SVC, Decision Tree
- Meta-model: Logistic Regression

**Regression Stack**

- Base models: Linear Regression, SVR, Decision Tree Regressor
- Meta-model: Linear Regression

### Evaluation Metrics

- Accuracy (Classification)
- R² Score (Regression)

---

## 5. Voting Ensemble

**File:** `voting-algorithm.ipynb`

### Problem Addressed

Simple and interpretable ensemble method for reducing variance without increasing complexity.

### Algorithm Intuition (Interview-Ready)

- Independent models vote on the outcome
- Wisdom of the crowd principle

### Voting Strategies

- **Hard Voting**: Majority class label
- **Soft Voting**: Average predicted probabilities

### Implementation Details (Production)

**Classification**

- Models: Logistic Regression, SVC, Decision Tree
- Ensemble: `VotingClassifier`

**Regression**

- Models: Linear Regression, SVR, Decision Tree
- Ensemble: `VotingRegressor`

### Evaluation Metrics

- Accuracy
- R² Score

---

## 6. XGBoost (Extreme Gradient Boosting)

**File:** `xg-boost-algo.ipynb`

### Problem Addressed

Traditional gradient boosting can be slow and prone to overfitting. XGBoost introduces **regularization and system-level optimizations**.

### Why XGBoost is Industry-Standard (Interview Gold)

- L1/L2 regularization
- Parallel tree construction
- Built-in handling of missing values
- Pruning via second-order gradients

### Implementation Details (Production)

- Model: `XGBClassifier`
- Hyperparameters:
  - `n_estimators=100`
  - `max_depth=3`
  - `learning_rate=0.1`
  - `eval_metric='logloss'`

### Evaluation Metrics

- Accuracy
- Classification Report

---

## Comparative Summary (Interview Perspective)

| Algorithm         | Strength                   | Limitation                |
| ----------------- | -------------------------- | ------------------------- |
| AdaBoost          | Focuses on hard samples    | Sensitive to noise        |
| Gradient Boosting | High accuracy              | Slower training           |
| XGBoost           | Best performance, scalable | More complex tuning       |
| Voting            | Simple, interpretable      | No learning of weights    |
| Stacking          | Learns optimal combination | Computationally expensive |

---

## Conclusion

This repository provides a **progressive learning path** through ensemble methods—from simple voting to advanced boosting techniques used in real-world systems. The implementations follow best practices suitable for **academic study, technical interviews, and production prototyping**.

---

### Tech Stack

- Python
- scikit-learn
- XGBoost
- NumPy

### Use Cases

- Machine Learning interviews
- Academic coursework and projects
- Rapid ensemble prototyping
