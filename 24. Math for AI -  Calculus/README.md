# 📊 Math for AI - Calculus

# Math for AI - Calculus

Calculus is the **engine behind learning in AI**.  
If Linear Algebra defines the _structure_ of models, **Calculus teaches models how to learn**.

Every time an AI model updates its weights, **calculus is at work**.

This document covers **Calculus from basics to advanced**, specifically focused on **Machine Learning and Deep Learning**.

---

## Table of Contents

1. Why Calculus for AI?
2. Functions and Graphs
3. Limits
4. Continuity
5. Derivatives – Intuition
6. Rules of Differentiation
7. Higher-Order Derivatives
8. Partial Derivatives
9. Gradients and Directional Derivatives
10. Chain Rule (Backpropagation Core)
11. Jacobian and Hessian
12. Optimization and Critical Points
13. Gradient Descent
14. Convexity
15. Integrals – Intuition
16. Definite and Indefinite Integrals
17. Multivariable Integrals
18. Taylor Series
19. Calculus in Machine Learning
20. Summary Cheat Sheet

---

## 1. Why Calculus for AI?

In AI, calculus is used to:

- Measure **how wrong** a model is (loss)
- Understand **how parameters affect loss**
- Decide **how to update parameters**
- Optimize models efficiently

Example:

```

Loss = f(weights)
Goal: minimize Loss

```

This requires:

- Derivatives
- Gradients
- Optimization methods

---

## 2. Functions and Graphs

A **function** maps inputs to outputs.

```

y = f(x)

```

Examples:

```

f(x) = x²
f(x) = 3x + 2
f(x) = sin(x)

```

**AI intuition:**

- Input → features
- Output → prediction

---

## 3. Limits

A **limit** describes what value a function approaches.

```

lim (x → a) f(x)

```

Example:

```

lim (x → 2) (x²) = 4

```

Limits form the foundation of derivatives and continuity.

---

## 4. Continuity

A function is continuous at `x = a` if:

1. `f(a)` exists
2. `lim (x → a) f(x)` exists
3. Both are equal

Most loss functions used in ML are **continuous**.

---

## 5. Derivatives – Intuition

A **derivative** measures **rate of change**.

```

Derivative = slope of tangent line

```

Example:

```

f(x) = x²
f'(x) = 2x

```

At `x = 3`:

```

slope = 6

```

**AI intuition:**

- How much does loss change when weights change?

---

## 6. Rules of Differentiation

### Power Rule

```

d/dx (xⁿ) = n xⁿ⁻¹

```

### Constant Rule

```

d/dx (c) = 0

```

### Sum Rule

```

d/dx (f + g) = f' + g'

```

### Exponential

```

d/dx (eˣ) = eˣ

```

### Logarithm

```

d/dx (ln x) = 1/x

```

---

## 7. Higher-Order Derivatives

Second derivative:

```

f''(x)

```

- Measures curvature
- Used to detect minima/maxima

Example:

```

f(x) = x²
f''(x) = 2 > 0 → minimum

```

---

## 8. Partial Derivatives

Used when functions have **multiple variables**.

```

f(x, y) = x² + y²

```

Partial derivatives:

```

∂f/∂x = 2x
∂f/∂y = 2y

```

**AI intuition:**
Each weight affects loss independently.

---

## 9. Gradients and Directional Derivatives

### Gradient Vector

```

∇f = [∂f/∂x₁, ∂f/∂x₂, ..., ∂f/∂xₙ]

```

Properties:

- Points in direction of **steepest increase**
- Negative gradient → steepest decrease

Used directly in **training neural networks**.

---

## 10. Chain Rule (Backpropagation Core)

The **most important rule in AI**.

If:

```

y = f(g(x))

```

Then:

```

dy/dx = f'(g(x)) · g'(x)

```

**Backpropagation = repeated application of chain rule**

---

## 11. Jacobian and Hessian

### Jacobian Matrix

Used for vector-valued functions.

```

J = ∂(outputs) / ∂(inputs)

```

### Hessian Matrix

Second-order partial derivatives.

```

H = ∂²f / ∂xᵢ∂xⱼ

```

Used in:

- Newton’s method
- Second-order optimization

---

## 12. Optimization and Critical Points

Critical points occur where:

```

∇f = 0

```

Types:

- Local minimum
- Local maximum
- Saddle point

Most ML problems aim for **local minima**.

---

## 13. Gradient Descent

Update rule:

```

θ = θ − α ∇L(θ)

```

Where:

- `θ` = parameters
- `α` = learning rate
- `L` = loss function

Variants:

- Batch Gradient Descent
- Stochastic Gradient Descent (SGD)
- Mini-batch Gradient Descent

---

## 14. Convexity

A function is **convex** if:

```

f(tx + (1−t)y) ≤ tf(x) + (1−t)f(y)

```

Why it matters:

- Convex loss → guaranteed global minimum

Examples:

- Mean Squared Error
- Logistic loss (convex)

---

## 15. Integrals – Intuition

An **integral** measures **accumulated change**.

```

∫ f(x) dx

```

Geometric meaning:

- Area under a curve

---

## 16. Definite and Indefinite Integrals

### Indefinite Integral

```

∫ x² dx = x³/3 + C

```

### Definite Integral

```

∫₀¹ x² dx = 1/3

```

Used in:

- Probability distributions
- Expectation values

---

## 17. Multivariable Integrals

```

∫∫ f(x, y) dx dy

```

Applications:

- Joint probability
- Continuous random variables

---

## 18. Taylor Series

Approximates functions using polynomials.

```

f(x) ≈ f(a) + f'(a)(x−a) + f''(a)/2!(x−a)² + ...

```

Used in:

- Optimization
- Numerical methods
- Understanding loss landscapes

---

## 19. Calculus in Machine Learning

| Concept       | ML Application            |
| ------------- | ------------------------- |
| Derivatives   | Loss sensitivity          |
| Gradients     | Weight updates            |
| Chain Rule    | Backpropagation           |
| Hessian       | Advanced optimization     |
| Integrals     | Probability & expectation |
| Taylor Series | Approximation & analysis  |

---

## 20. Summary Cheat Sheet

- **Derivatives** → how fast loss changes
- **Gradients** → direction to move parameters
- **Chain rule** → learning in neural networks
- **Optimization** → minimize loss
- **Integrals** → probability & statistics

> If Linear Algebra builds the model, **Calculus teaches it how to learn**.

---

## Next Steps

- 📐 Probability & Statistics for AI
- 🧠 Optimization Algorithms
- 💻 Implement with NumPy, PyTorch, TensorFlow

---

### ⭐ If this helped you, consider starring the repository!

```

```
