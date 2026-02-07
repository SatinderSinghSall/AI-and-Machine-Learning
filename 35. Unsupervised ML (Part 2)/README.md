# Thyroid Disease Anomaly Detection using Unsupervised Machine Learning

## 📌 Project Overview

This project implements and compares **four unsupervised machine learning algorithms** to detect anomalies (outliers) in a medical thyroid dataset.

Anomaly detection is critical in healthcare analytics because rare or abnormal records may indicate:

- Disease conditions
- Measurement errors
- Unusual patient profiles
- Data corruption

Since anomalies are **rare and often unlabeled**, we apply **unsupervised learning techniques** that detect abnormal behavior without relying on class labels.

---

## 🎯 Objectives

The main goals of this project are:

1. Understand dimensionality reduction using PCA
2. Apply density-based anomaly detection (DBSCAN)
3. Apply tree-based anomaly detection (Isolation Forest)
4. Apply local density-based detection (LOF)
5. Compare performance and behavior of each algorithm
6. Visualize anomalies for interpretability

---

## 📂 Repository Structure

```
.
├── pca-algorithm.ipynb
├── DBSCAN-Anomaly.ipynb
├── Isolation-Forest-Algo.ipynb
├── LOF-Algorithm.ipynb
├── thyroid_dataset.csv
└── README.md
```

---

# 📊 Dataset Description

## Thyroid Dataset

**File:** `thyroid_dataset.csv`

### Characteristics

- Samples: 6916 patients
- Features: 21 medical attributes
- Target: `Outlier_label`

### Example Features

- Age
- Sex
- Hormone measurements
- Medication indicators
- Diagnostic flags

### Why anomaly detection?

Medical datasets typically contain:

- Very few abnormal cases
- Imbalanced classes
- Hidden pathological patterns

Thus, unsupervised detection is appropriate.

---

# ⚙️ Algorithms Implemented

This project implements four major techniques:

| Algorithm        | Category                 | Purpose                   |
| ---------------- | ------------------------ | ------------------------- |
| PCA              | Dimensionality Reduction | Visualization             |
| DBSCAN           | Density-based            | Cluster + noise detection |
| Isolation Forest | Tree-based               | Global anomaly detection  |
| LOF              | Local density-based      | Local anomaly detection   |

---

---

# 1️⃣ Principal Component Analysis (PCA)

## Notebook

`pca-algorithm.ipynb`

## Purpose

PCA is **not an anomaly detector**, but a **dimensionality reduction technique** used for:

- Visualization
- Noise reduction
- Feature compression
- Faster modeling

---

## Mathematical Intuition

PCA finds directions that maximize variance.

Steps:

1. Standardize features
2. Compute covariance matrix
3. Compute eigenvectors
4. Project data onto top components

Projection:

[
Z = XW
]

where

- X = original data
- W = principal components
- Z = reduced data

---

## Workflow

```
Load data
→ Standardize
→ Apply PCA (2 components)
→ Plot 2D projection
```

---

## Use Case in Project

Used to:

- Visualize anomalies detected by other algorithms
- Reduce high-dimensional thyroid data to 2D

---

---

# 2️⃣ DBSCAN (Density-Based Spatial Clustering)

## Notebook

`DBSCAN-Anomaly.ipynb`

## Concept

DBSCAN groups points based on **density** rather than distance from centroids.

Key idea:

- Dense region → cluster
- Sparse region → anomaly

---

## Parameters

| Parameter   | Meaning                       |
| ----------- | ----------------------------- |
| eps         | neighborhood radius           |
| min_samples | minimum neighbors for cluster |

---

## Classification Rules

- Core point → enough neighbors
- Border point → near cluster
- Noise point → anomaly

Noise label:

```
-1 → anomaly
```

---

## Algorithm Steps

```
For each point:
   Count neighbors within eps
   If neighbors >= min_samples → core
   Else → noise
```

---

## Workflow

```
Generate data
→ Scale
→ Apply DBSCAN
→ Label clusters
→ Noise = anomaly
→ Visualize
```

---

## Advantages

✔ No need to specify number of clusters
✔ Detects arbitrary shapes
✔ Automatically finds noise

## Limitations

✘ Sensitive to eps
✘ Struggles with varying density

---

---

# 3️⃣ Isolation Forest

## Notebook

`Isolation-Forest-Algo.ipynb`

## Concept

Isolation Forest isolates anomalies using **random tree splits**.

Key principle:

> Anomalies are easier to isolate and require fewer splits.

---

## Mathematical Idea

Average path length:

[
score(x) = 2^{-\frac{E(h(x))}{c(n)}}
]

- shorter path → more anomalous

---

## Parameters

| Parameter     | Meaning               |
| ------------- | --------------------- |
| n_estimators  | number of trees       |
| contamination | expected anomaly rate |
| random_state  | reproducibility       |

---

## Workflow

```
Load thyroid dataset
→ Scale features
→ Train Isolation Forest
→ Predict labels
→ PCA visualization
→ Count anomalies
```

---

## Advantages

✔ Very fast
✔ Works well for high dimensions
✔ Scales to large datasets
✔ Minimal parameter tuning

## Limitations

✘ Global only (misses local anomalies sometimes)

---

---

# 4️⃣ Local Outlier Factor (LOF)

## Notebook

`LOF-Algorithm.ipynb`

## Concept

LOF compares **local density** of a point to neighbors.

If a point is less dense than neighbors → anomaly.

---

## Mathematical Intuition

Local reachability density:

[
LOF(p) = \frac{average\ density\ of\ neighbors}{density(p)}
]

If:

```
LOF ≈ 1 → normal
LOF >> 1 → anomaly
```

---

## Workflow

```
Load thyroid dataset
→ Scale
→ Fit LOF
→ Predict outliers
→ PCA visualization
```

---

## Advantages

✔ Detects local anomalies
✔ Works well for clusters of varying density

## Limitations

✘ Computationally expensive
✘ Slower on large datasets

---

---

# 📈 Visual Pipeline (Complete Project)

```
Raw Dataset
    ↓
Standard Scaling
    ↓
Isolation Forest / LOF / DBSCAN
    ↓
Outlier Labels
    ↓
PCA (2D)
    ↓
Visualization
```

---

# 📊 Algorithm Comparison

| Method           | Type      | Speed     | Local detection | Best for            |
| ---------------- | --------- | --------- | --------------- | ------------------- |
| PCA              | Reduction | Fast      | No              | Visualization       |
| DBSCAN           | Density   | Medium    | Yes             | Non-linear shapes   |
| Isolation Forest | Tree      | Very Fast | No              | Large/high-dim data |
| LOF              | Density   | Slow      | Yes             | Local anomalies     |

---

# 🧪 Suggested Evaluation Metrics

Since labels exist:

- Precision
- Recall
- F1-score
- ROC-AUC
- Confusion Matrix

Example:

```python
from sklearn.metrics import classification_report
print(classification_report(y_true, y_pred))
```

---

# ▶️ How to Run

## Install dependencies

```bash
pip install numpy pandas matplotlib seaborn scikit-learn jupyter
```

## Launch notebooks

```bash
jupyter notebook
```

Run notebooks in order:

1. pca-algorithm.ipynb
2. DBSCAN-Anomaly.ipynb
3. Isolation-Forest-Algo.ipynb
4. LOF-Algorithm.ipynb

---

# 💼 Professional Applications

These methods are widely used in:

- Healthcare diagnostics
- Fraud detection
- Cybersecurity
- Fault detection
- Manufacturing QA
- Financial risk analysis

---

# 📚 Key Takeaways

- PCA helps visualization
- DBSCAN detects shape-based noise
- Isolation Forest is fastest and scalable
- LOF detects subtle local anomalies
- Combining methods improves robustness

---

# 🚀 Future Improvements

Possible extensions:

- Hyperparameter tuning
- Cross-validation
- Ensemble anomaly detection
- Autoencoders (deep learning)
- SHAP explainability
- Real-time detection

---

# 👨‍💻 Author

Satinder Singh Sall

Machine Learning Anomaly Detection Project
Academic + Professional Demonstration

---

# 📜 License

For educational and research purposes only.

---

> **Unsupervised Anomaly Detection on Thyroid dataset + PCA visualization**

---

# 📁 1) `DBSCAN-Anomaly.ipynb`

**Goal:** Detect anomalies using **DBSCAN clustering** on synthetic data.

---

### Cell 0 — Markdown

Introduces:

- DBSCAN
- Density-based clustering
- Unsupervised anomaly detection

---

### Cell 1 — Imports

```python
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_moons
```

Used for:

- Visualization
- Scaling
- Clustering
- Synthetic dataset

---

### Cell 3 — Generate Data

```python
X, y = make_moons(n_samples=500, noise=0.1, random_state=42)
```

Creates:

- 500 curved moon-shaped points
- Noise added
- Perfect for DBSCAN because clusters are non-linear

---

### Cell 4

Displays raw data.

---

### Cell 6 — Scaling

```python
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

Why?

- DBSCAN uses **distance**
- Distance requires normalized features

---

### Cell 8 — Plot

```python
sns.scatterplot(...)
```

Shows shape of moons.

---

### Cell 10 — DBSCAN model

```python
DBSCAN(eps=0.18, min_samples=5)
```

Key parameters:

- `eps` → neighborhood radius
- `min_samples` → density threshold

---

### Cell 11 — Fit + predict

```python
labels = dbscan.fit_predict(X_scaled)
```

Outputs:

- cluster id
- `-1` = anomaly (noise)

---

### Cell 13 — Visualization

Colored scatter plot:

- clusters
- anomalies

---

### ✅ Summary

Pipeline:

```
Generate → Scale → DBSCAN → Label → Visualize
```

Good for:

- non-linear clusters
- density-based anomaly detection

---

# 📁 2) `Isolation-Forest-Algo.ipynb`

**Goal:** Detect anomalies in real **thyroid medical dataset**

---

### Cell 1 — Imports

Includes:

- pandas
- matplotlib
- StandardScaler
- IsolationForest
- PCA

---

### Cell 3 — Load dataset

```python
df = pd.read_csv("thyroid_dataset.csv")
```

Dataset:

```
Rows: 6916
Columns: 22
```

Includes:

- medical features
- `Outlier_label`

---

### Cell 6 — Separate X and y

```python
X = df.drop("Outlier_label", axis=1)
y = df["Outlier_label"]
```

Even though unsupervised, label is used for evaluation.

---

### Cell 8 — Scaling

```python
StandardScaler()
```

Important for tree isolation fairness.

---

### Cell 10 — Isolation Forest

```python
IsolationForest(
    n_estimators=200,
    contamination=0.036,
    random_state=42
)
```

Parameters:

- trees = 200
- contamination = expected anomaly %
- random_state = reproducible

---

### Cell 12 — Predict

```python
labels = clf.fit_predict(X_scaled)
```

Outputs:

- 1 = normal
- -1 = anomaly

---

### Cell 14–15 — PCA visualization

```python
PCA(n_components=2)
plt.scatter(...)
```

Used only to:

- reduce dimension
- plot anomalies

---

### Cell 17 — Count anomalies

```python
np.sum(labels == -1)
```

---

### ✅ Summary

Pipeline:

```
Load → Scale → IsolationForest → Predict → PCA → Plot → Count
```

Best for:

- high dimensional data
- fast
- robust

---

# 📁 3) `LOF-Algorithm.ipynb`

**Goal:** Compare **Isolation Forest + LOF**

---

### Cells 0–18

⚠️ **Duplicate of Isolation Forest section**
Runs same process as previous notebook first.

---

## New section starts at Cell 19

---

### Cell 20 — LOF model

```python
LocalOutlierFactor(contamination=0.036)
```

LOF logic:

- compares density of point vs neighbors
- lower density → anomaly

---

### Cell 22 — Predict

```python
labels = neighbors.fit_predict(X_scaled)
```

Again:

- -1 anomaly
- 1 normal

---

### Cell 24–25 — PCA plot

Same as before.

---

### Cell 27 — Count anomalies

---

### ⚠️ Issues to fix

1. Title still says Isolation Forest in LOF section
2. Unnecessary duplicate Isolation Forest block
3. Could compare results side-by-side

---

### ✅ Summary

Pipeline:

```
Load → Scale → LOF → Predict → PCA → Plot
```

Best for:

- local density anomalies
- cluster-dependent outliers

---

# 📁 4) `pca-algorithm.ipynb`

**Goal:** Demonstrate PCA using Iris dataset

---

### Cell 1 — Imports

---

### Cell 3 — Load Iris

```python
load_iris()
```

Data:

- 150 samples
- 4 features
- 3 classes

---

### Cell 6 — Scaling

Important because PCA depends on variance.

---

### Cell 8 — PCA

```python
PCA(n_components=2)
```

Reduces:

```
4D → 2D
```

---

### Cell 11 — Explained variance

```python
pca.explained_variance_ratio_
```

Shows:

- how much information kept

Usually ~95% for Iris

---

### Cell 13 — Plot

Colored by species.

---

### ✅ Summary

Pipeline:

```
Load → Scale → PCA → Variance → Plot
```

Pure dimensionality reduction demo.

---

# 📁 5) `thyroid_dataset.csv`

### Shape

```
6916 rows × 22 columns
```

### Typical columns:

- Age
- Sex
- medication flags
- thyroid hormone levels
- Outlier_label

Used in:

- Isolation Forest
- LOF

---

# 🎯 Big Picture (How all notebooks connect)

### Flow of your project:

```
PCA basics (iris)
      ↓
Synthetic anomaly detection (DBSCAN)
      ↓
Real dataset anomaly detection
      ↓
Compare algorithms:
   Isolation Forest
   LOF
```

---

# 📊 Algorithm Comparison

| Algorithm        | Strength             | Weakness          |
| ---------------- | -------------------- | ----------------- |
| DBSCAN           | shape-based clusters | sensitive eps     |
| Isolation Forest | fast, scalable       | global only       |
| LOF              | local density aware  | slow for big data |
| PCA              | visualization only   | not detector      |

---

# 💡 Suggestions to Improve

### 1. Compare algorithms together

Add:

```python
from sklearn.metrics import classification_report
print(classification_report(y, labels))
```

---

### 2. Avoid duplicate code

Create reusable functions:

```python
def scale_data(X):
    return StandardScaler().fit_transform(X)
```

---

### 3. Tune contamination automatically

```python
contamination = y.mean()
```

---

### 4. Add metrics

- Precision
- Recall
- F1
- ROC curve
