# Unsupervised Learning – Clustering Algorithms from Scratch & Scikit-Learn

## 📌 Project Overview

This repository provides an in-depth academic and practical exploration of **unsupervised learning**, specifically **clustering algorithms**.

The goal is to understand how different clustering techniques behave on:

• Synthetic datasets  
• Real-world datasets (Iris)  
• Linear vs non-linear cluster structures

The project demonstrates:

- K-Means Clustering
- DBSCAN (Density-Based Spatial Clustering)
- Hierarchical (Agglomerative) Clustering
- PCA for visualization
- Cluster evaluation metrics
- Elbow Method
- Silhouette Analysis

This repository is designed for:

✔ Students learning Machine Learning  
✔ Interview preparation  
✔ Academic lab work  
✔ Conceptual + hands-on understanding

---

# 📚 Table of Contents

1. Introduction to Clustering
2. Mathematical Foundations
3. Algorithms Implemented
   - K-Means
   - K-Means on Iris
   - DBSCAN
   - Hierarchical Clustering
4. Evaluation Metrics
5. Dataset Descriptions
6. Notebook Descriptions
7. Algorithm Comparison
8. When to Use What
9. Installation
10. Usage
11. Results Summary
12. Future Improvements
13. References

---

# 1️⃣ Introduction to Clustering

Clustering is an **unsupervised learning technique** used to group similar data points together without labeled outputs.

Unlike supervised learning:

- No target variable
- No ground truth during training
- Structure discovered automatically

Applications include:

- Customer segmentation
- Image segmentation
- Anomaly detection
- Market basket analysis
- Bioinformatics
- Pattern recognition

---

# 2️⃣ Mathematical Foundations

## Distance Metrics

Most clustering algorithms depend on distance:

### Euclidean Distance

\[
d(x,y) = \sqrt{\sum\_{i=1}^{n}(x_i - y_i)^2}
\]

### Importance of Scaling

Features must be standardized:

\[
z = \frac{x - \mu}{\sigma}
\]

Without scaling:

- Larger features dominate
- Incorrect clusters form

---

# 3️⃣ Algorithms Implemented

---

# 🔵 K-Means Clustering

## Concept

Partition data into **K clusters** by minimizing variance inside each cluster.

## Objective Function

\[
WCSS = \sum*{i=1}^{k}\sum*{x \in C_i} ||x - \mu_i||^2
\]

Where:

- \( \mu_i \) = centroid

## Algorithm Steps

1. Choose K
2. Initialize centroids randomly
3. Assign points to nearest centroid
4. Update centroids
5. Repeat until convergence

## Properties

Advantages:
✔ Fast  
✔ Simple  
✔ Scales well

Limitations:
✖ Must choose K  
✖ Poor for non-linear shapes  
✖ Sensitive to initialization  
✖ Sensitive to outliers

---

# 🔵 K-Means on Iris Dataset

This notebook applies K-Means to a real dataset.

Includes:

- Feature scaling
- PCA dimensionality reduction
- Elbow method
- Visualization
- Cluster vs true labels comparison

Purpose:
Demonstrate practical clustering on real-world data.

---

# 🔵 DBSCAN (Density-Based Clustering)

## Concept

Groups points based on **density**, not distance to centroid.

Clusters = regions with many nearby points.

## Key Terms

- eps → radius
- min_samples → minimum neighbors
- core point
- border point
- noise point

## Algorithm Steps

1. Pick point
2. Count neighbors within eps
3. If neighbors ≥ min_samples → cluster
4. Expand cluster recursively

## Properties

Advantages:
✔ Finds arbitrary shapes  
✔ Detects noise  
✔ No need to specify K

Limitations:
✖ Hard to tune eps  
✖ Poor with varying densities  
✖ Slower than KMeans

---

# 🔵 Hierarchical Clustering (Agglomerative)

## Concept

Builds clusters in a **tree structure (dendrogram)**.

Bottom-up approach:

- Each point starts as cluster
- Merge closest clusters repeatedly

## Linkage Methods

- Single
- Complete
- Average
- Ward (used in this project)

Ward minimizes variance increase.

## Properties

Advantages:
✔ No need to choose K initially  
✔ Visual dendrogram  
✔ Interpretable

Limitations:
✖ Expensive computationally  
✖ Not scalable  
✖ Once merged cannot undo

---

# 4️⃣ Evaluation Metrics

## Elbow Method

WCSS vs K → find “elbow”

## Silhouette Score

\[
s = \frac{b-a}{max(a,b)}
\]

Range:
-1 → bad  
+1 → good

## Inertia

Within-cluster variance

## Additional (optional)

- Davies–Bouldin Index
- Calinski–Harabasz Score

---

# 5️⃣ Dataset Descriptions

## Synthetic Data (make_blobs)

Used for:

- Testing KMeans
- Known cluster centers

## make_moons

Used for:

- DBSCAN demonstration
- Non-linear clusters

## Iris Dataset

150 samples, 4 features:

- sepal length
- sepal width
- petal length
- petal width

3 species:

- setosa
- versicolor
- virginica

---

# 6️⃣ Notebook Descriptions

## 📁 KMeans-Algorithm.ipynb

Covers:

- Synthetic blobs
- Elbow method
- Silhouette score
- Knee detection
- Visualization

Most complete demonstration of KMeans.

---

## 📁 KMeans-Iris-Dataset.ipynb

Covers:

- Real data clustering
- PCA
- Centroids visualization
- True vs predicted comparison

Focus: practical application

---

## 📁 DBSCAN-Algorithm.ipynb

Covers:

- Density clustering
- Parameter tuning
- Comparison with KMeans
- Works on non-linear shapes

Shows where KMeans fails.

---

## 📁 Hierarchial-Clustering-Algo.ipynb

Covers:

- Linkage
- Dendrogram
- Agglomerative clustering
- Ward method

Focus: tree-based clustering

---

# 7️⃣ Algorithm Comparison

| Feature           | KMeans | DBSCAN    | Hierarchical |
| ----------------- | ------ | --------- | ------------ |
| Need K            | Yes    | No        | Optional     |
| Handles noise     | No     | Yes       | Partial      |
| Shape flexibility | Poor   | Excellent | Good         |
| Speed             | Fast   | Medium    | Slow         |
| Scalability       | High   | Medium    | Low          |
| Deterministic     | No     | Yes       | Yes          |

---

# 8️⃣ When to Use What

Use KMeans:

- spherical clusters
- large datasets

Use DBSCAN:

- irregular shapes
- noise detection

Use Hierarchical:

- small datasets
- need interpretability

---

# 9️⃣ Installation

```bash
pip install numpy pandas matplotlib seaborn scikit-learn scipy kneed
```

````

---

# 🔟 Usage

Open notebooks:

```bash
jupyter notebook
```

Run sequentially.

---

# 1️⃣1️⃣ Results Summary

Observations:

- KMeans performs best on blob-like clusters
- DBSCAN excels on non-linear structures
- Hierarchical provides interpretable dendrograms
- PCA improves visualization clarity
- Scaling is mandatory

---

# 1️⃣2️⃣ Future Improvements

Possible extensions:

- DBSCAN parameter tuning (k-distance plot)
- HDBSCAN
- Spectral clustering
- Gaussian Mixture Models
- Automatic K selection
- Performance benchmarking
- Interactive plots

---

# 1️⃣3️⃣ References

- Scikit-Learn Documentation
- Pattern Recognition and Machine Learning – Bishop
- Hands-On Machine Learning – Géron
- Machine Learning – Tom Mitchell

---

# 👨‍💻 Author

Satinder Singh Sall

Clustering Algorithms Study & Implementation
Educational / Academic project
````
