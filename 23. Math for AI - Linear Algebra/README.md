# 📊 Math for AI – Linear Algebra

# Math for AI – Linear Algebra

Linear Algebra is the **core mathematical language of Artificial Intelligence and Machine Learning**.  
Almost everything in AI — data, models, training, optimization — is expressed using vectors, matrices, and linear transformations.

This document covers **Linear Algebra from basic to advanced**, with **examples and AI intuition**.

---

## Table of Contents

1. Why Linear Algebra for AI?
2. Scalars, Vectors, and Matrices
3. Vector Operations
4. Matrix Operations
5. Systems of Linear Equations
6. Vector Spaces
7. Linear Transformations
8. Matrix Properties
9. Determinants
10. Matrix Inverse
11. Rank and Null Space
12. Eigenvalues and Eigenvectors
13. Diagonalization
14. Orthogonality and Orthonormal Bases
15. Projections
16. Singular Value Decomposition (SVD)
17. Norms and Distance Measures
18. Quadratic Forms
19. Linear Algebra in Machine Learning
20. Summary Cheat Sheet

---

## 1. Why Linear Algebra for AI?

In AI:

- **Data** → vectors and matrices
- **Models** → matrix transformations
- **Predictions** → dot products
- **Training** → solving linear systems
- **Dimensionality reduction** → eigenvalues & SVD

Example:

- An image (28×28 pixels) → a **784-dimensional vector**
- A dataset → a **matrix**
- Neural network layers → **matrix multiplications**

---

## 2. Scalars, Vectors, and Matrices

### Scalar

A single number.

```

a = 5

```

### Vector

An ordered list of numbers.

```

v = [2, 4, 6]

```

Column vector:

```

v = ⎡2⎤
⎢4⎥
⎣6⎦

```

### Matrix

A 2D array of numbers.

```

A = ⎡1 2⎤
⎣3 4⎦

```

**AI intuition:**

- Vector → one data point
- Matrix → dataset

---

## 3. Vector Operations

### Vector Addition

```

[1, 2] + [3, 4] = [4, 6]

```

### Scalar Multiplication

```

2 × [1, 3] = [2, 6]

```

### Dot Product

```

[1, 2] · [3, 4] = 1×3 + 2×4 = 11

```

**Interpretation:**

- Measures similarity between vectors
- Used in cosine similarity and neural networks

---

## 4. Matrix Operations

### Matrix Addition

```

A + B = element-wise addition

```

### Matrix Multiplication

```

A (m×n) × B (n×p) = C (m×p)

```

Example:

```

⎡1 2⎤ ⎡5 6⎤ ⎡19 22⎤
⎣3 4⎦ × ⎣7 8⎦ = ⎣43 50⎦

```

**AI intuition:**

- Core operation in neural networks
- Each layer = matrix multiplication + bias

---

## 5. Systems of Linear Equations

Example:

```

2x + y = 5
x - y = 1

```

Matrix form:

```

Ax = b

```

```

⎡2 1⎤ ⎡x⎤ = ⎡5⎤
⎣1 -1⎦⎣y⎦ ⎣1⎦

```

Solutions found using:

- Gaussian elimination
- Matrix inverse (if exists)

---

## 6. Vector Spaces

A **vector space** satisfies:

- Closure under addition
- Closure under scalar multiplication
- Zero vector exists
- Additive inverse exists

Examples:

- ℝⁿ
- Polynomial spaces
- Function spaces

**AI intuition:**
Feature vectors live in vector spaces.

---

## 7. Linear Transformations

A function `T(v)` is linear if:

```

T(u + v) = T(u) + T(v)
T(cv) = cT(v)

```

Represented using matrices:

```

T(v) = Av

```

Examples:

- Rotation
- Scaling
- Reflection

---

## 8. Matrix Properties

### Transpose

```

Aᵀ

```

### Symmetric Matrix

```

A = Aᵀ

```

### Identity Matrix

```

I = ⎡1 0⎤
⎣0 1⎦

```

### Zero Matrix

All elements are zero.

---

## 9. Determinants

For 2×2 matrix:

```

A = ⎡a b⎤
⎣c d⎦

det(A) = ad − bc

```

**Meaning:**

- Area/volume scaling factor
- det = 0 → matrix is singular (not invertible)

---

## 10. Matrix Inverse

If `A⁻¹` exists:

```

A A⁻¹ = I

```

Solution to:

```

Ax = b

```

is:

```

x = A⁻¹b

```

**AI note:**
Direct inversion is expensive; usually avoided in ML.

---

## 11. Rank and Null Space

### Rank

- Number of linearly independent columns

### Null Space

All vectors `x` such that:

```

Ax = 0

```

**Interpretation:**

- Rank → information content
- Null space → lost information

---

## 12. Eigenvalues and Eigenvectors

Definition:

```

Av = λv

```

- `v` → eigenvector
- `λ` → eigenvalue

Example:

```

A = ⎡2 0⎤
⎣0 3⎦

```

Eigenvalues: `2, 3`

**AI intuition:**

- Principal directions of data
- Core of PCA

---

## 13. Diagonalization

If possible:

```

A = PDP⁻¹

```

Where:

- `D` is diagonal (eigenvalues)
- `P` contains eigenvectors

Speeds up:

- Matrix powers
- Computations

---

## 14. Orthogonality and Orthonormal Bases

### Orthogonal Vectors

```

v · w = 0

```

### Orthonormal

- Orthogonal
- Unit length

Used in:

- QR decomposition
- PCA
- Signal processing

---

## 15. Projections

Projection of `v` onto `u`:

```

projᵤ(v) = (v·u / u·u) u

```

**AI intuition:**

- Feature projection
- Dimensionality reduction

---

## 16. Singular Value Decomposition (SVD)

Any matrix:

```

A = U Σ Vᵀ

```

Where:

- `U` → left singular vectors
- `Σ` → singular values
- `V` → right singular vectors

Applications:

- PCA
- Noise reduction
- Recommendation systems

---

## 17. Norms and Distance Measures

### L2 Norm (Euclidean)

```

||v||₂ = √(v₁² + v₂² + ...)

```

### L1 Norm

```

||v||₁ = |v₁| + |v₂| + ...

```

### Cosine Similarity

```

(v·w) / (||v|| ||w||)

```

Used in:

- Similarity search
- NLP embeddings

---

## 18. Quadratic Forms

```

xᵀAx

```

Used in:

- Loss functions
- Optimization
- Regularization

Example:

- Mean Squared Error

---

## 19. Linear Algebra in Machine Learning

| Concept      | ML Application           |
| ------------ | ------------------------ |
| Vectors      | Feature representation   |
| Matrices     | Datasets, weights        |
| Dot product  | Predictions              |
| Eigenvectors | PCA                      |
| SVD          | Dimensionality reduction |
| Norms        | Regularization           |
| Projections  | Feature extraction       |

---

## 20. Summary Cheat Sheet

- **Data** → vectors & matrices
- **Models** → linear transformations
- **Training** → solving linear systems
- **Optimization** → quadratic forms
- **Dimensionality reduction** → eigenvalues & SVD

> Mastering Linear Algebra = Understanding how AI thinks mathematically.

---

## Next Steps

- Study **Calculus for AI**
- Study **Probability & Statistics**
- Implement concepts using **NumPy & PyTorch**

---

### ⭐ If you found this useful, consider starring the repository!

```

```
