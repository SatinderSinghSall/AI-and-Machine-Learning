# Artificial Intelligence and Machine Learning: AI / ML

Below is a **complete, professional & academic-quality `README.md`** you can use for your Deep Learning Part 1 → Part 2 learning and neuron implementation project.

It is written to:

✅ look professional on GitHub
✅ help in academic submissions
✅ impress recruiters & interviewers
✅ serve as revision notes
✅ include theory + math + examples

You can copy & paste directly into **README.md**.

---

# 🧠 Deep Learning Fundamentals & Neural Network Implementation

## 📌 Overview

This project documents my learning journey through **Deep Learning (Part 1 & Part 2)** and includes:

- Core deep learning theory
- Neural network fundamentals
- Forward & backward propagation
- Loss functions & optimization
- Activation functions & training mechanics
- Vanishing gradient problem
- Implementation of an artificial neuron using **PyTorch**
- Mathematical understanding of neural computation

This repository serves both **academic learning** and **professional reference**.

---

# 🎯 Learning Objectives

By completing these modules and implementation exercises, I gained the ability to:

✔ Understand deep learning fundamentals
✔ Build and interpret neural networks
✔ Understand forward & backward propagation
✔ Apply loss functions for regression & classification
✔ Train neural networks using gradient descent
✔ Diagnose vanishing gradient issues
✔ Use activation functions effectively
✔ Implement a neuron mathematically and programmatically

---

# 📚 Deep Learning — Part 1

## 1️⃣ What is Deep Learning?

Deep Learning is a subset of Machine Learning that uses **multi-layer neural networks** to learn patterns from data.

### 🔹 Key Characteristics

- Learns hierarchical features automatically
- Handles large datasets
- Excelling in vision, speech & NLP tasks

### 🔹 Real-world Applications

- Face recognition
- Self-driving cars
- Medical diagnosis
- Voice assistants

---

## 2️⃣ Machine Learning vs Deep Learning

| Feature             | Machine Learning | Deep Learning |
| ------------------- | ---------------- | ------------- |
| Feature Engineering | Manual           | Automatic     |
| Data Requirement    | Moderate         | Large         |
| Performance         | Good             | Excellent     |
| Hardware            | CPU              | GPU preferred |

---

## 3️⃣ What are Neural Networks?

A neural network is a mathematical model inspired by the human brain.

### 🔹 Biological vs Artificial Neuron

Biological neuron:

- dendrites → inputs
- soma → processing
- axon → output

Artificial neuron:

[
y = \sum w_i x_i + b
]

Where:

- (x) = inputs
- (w) = weights
- (b) = bias

---

## 4️⃣ Perceptron (Single Neuron Model)

The perceptron is the simplest neural network unit.

### 🔹 Mathematical Model

[
z = w_1x_1 + w_2x_2 + ... + b
]

[
y = f(z)
]

### 🔹 Activation (Step Function)

Used for binary classification.

### 🔹 Decision Boundary

Perceptron creates a **linear boundary**.

⚠ Limitation: cannot solve non-linear problems like XOR.

---

## 5️⃣ Multi-Layer Neural Networks

To solve complex problems, multiple layers are used.

### 🔹 Structure

Input Layer → Hidden Layers → Output Layer

### 🔹 Why Hidden Layers?

They enable learning of:

- patterns
- shapes
- complex relationships

Example:

- First layer: edges
- Second: shapes
- Third: objects

---

## 6️⃣ Deep Learning Frameworks

### 🔹 PyTorch

- Dynamic computation graph
- Python-friendly
- Research oriented

### 🔹 TensorFlow

- Production-ready
- Scalable deployment

### 🔹 Keras

- High-level API
- Beginner friendly

---

## 7️⃣ Building a Neuron in Code

Understanding neurons through implementation improves conceptual clarity.

Key components:

- inputs
- weights
- bias
- output

---

# 📚 Deep Learning — Part 2

## 1️⃣ Forward Propagation

Forward propagation computes predictions.

### Steps:

1. Multiply inputs by weights
2. Add bias
3. Apply activation function
4. Produce output

[
y = f(WX + b)
]

---

## 2️⃣ Loss Functions

Loss measures prediction error.

---

### 🔹 Regression Loss

#### Mean Squared Error (MSE)

[
MSE = \frac{1}{n}\sum(y_{true}-y_{pred})^2
]

**Use Case:** price prediction

---

### 🔹 Classification Loss

#### Binary Cross Entropy

[
L = -[y\log(p) + (1-y)\log(1-p)]
]

**Use Case:** spam detection

---

## 3️⃣ Backpropagation

Backpropagation updates weights by computing gradients.

### 🔹 Key Idea

Use **chain rule** to compute error contribution of each weight.

### 🔹 Steps

1. Compute loss
2. Calculate gradients
3. Update weights

---

## 4️⃣ Chain Rule in Neural Networks

Used to compute gradients layer by layer.

[
\frac{dL}{dw} = \frac{dL}{dz} \cdot \frac{dz}{dw}
]

This allows error to flow backward.

---

## 5️⃣ Weight & Bias Update (Gradient Descent)

[
w = w - \eta \frac{\partial L}{\partial w}
]

Where:

- (\eta) = learning rate

---

## 6️⃣ Vanishing Gradient Problem

In deep networks, gradients can become extremely small.

### 🔹 Effects

- slow learning
- early layers stop training

### 🔹 Causes

Sigmoid & tanh activation functions.

---

## 7️⃣ Activation Functions

### 🔹 ReLU (Rectified Linear Unit)

[
f(x) = max(0,x)
]

✔ prevents vanishing gradient
✔ fast computation

### 🔹 Variants

- Leaky ReLU
- Parametric ReLU

---

## 8️⃣ Batch vs Iteration vs Epoch

| Term      | Meaning           |
| --------- | ----------------- |
| Batch     | subset of data    |
| Iteration | one batch pass    |
| Epoch     | full dataset pass |

---

## 9️⃣ Optimizers

Optimizers adjust weights efficiently.

### 🔹 SGD

Basic gradient descent.

### 🔹 Adam

Adaptive learning rate
Faster convergence.

---

# 🧠 Neuron Implementation (PyTorch)

## 📌 Code Example

```python
import torch
import torch.nn as nn

torch.manual_seed(42)

inputs = torch.tensor([1.0, 2.0, 3.0])

neuron = nn.Linear(3, 1)

output = neuron(inputs)

print(output)
```

---

## 🔍 What This Code Does

### Step 1: Import Libraries

Provides tensor operations & neural network tools.

### Step 2: Set Seed

Ensures reproducible results.

### Step 3: Define Inputs

Represents feature vector.

### Step 4: Create Neuron

Implements:

[
y = W\cdot X + b
]

### Step 5: Forward Pass

Computes neuron output.

---

## 🔍 Inspecting Parameters

```python
neuron.weight
neuron.bias
```

These are **learnable parameters**.

---

## 🔍 Manual Verification

```python
neuron.weight @ inputs + neuron.bias
```

Confirms internal computation.

---

# 🧪 Example Output Interpretation

If:

Weights = `[0.5, -0.2, 0.1]`
Bias = `0.3`

Input = `[1,2,3]`

[
y = (0.5×1) + (-0.2×2) + (0.1×3) + 0.3
]

[
y = 0.5 - 0.4 + 0.3 + 0.3 = 0.7
]

---

# 🧩 Concepts Mastered

## 🔹 Theory

✔ Neural networks
✔ Perceptron & multi-layer networks
✔ Forward & backward propagation
✔ Loss functions
✔ Optimization & gradient descent
✔ Activation functions
✔ Vanishing gradient problem

## 🔹 Practical Skills

✔ PyTorch fundamentals
✔ Tensor operations
✔ Implementing artificial neurons
✔ Understanding weights & bias
✔ Forward pass computation

---

# 🚀 Professional Applications

These concepts are foundational for:

- Computer Vision
- NLP systems
- Recommendation systems
- Fraud detection
- Autonomous systems
- AI research & development

---

# 🎓 Academic Relevance

This project demonstrates understanding of:

- Neural computation mathematics
- Gradient-based optimization
- Deep learning architecture
- Practical neural network implementation

---

# 📌 Future Enhancements

⬜ Build multi-layer neural network
⬜ Implement backpropagation manually
⬜ Train on real dataset
⬜ Visualize training process
⬜ Build classification model

---

# 👤 Author

**Satinder Singh**

Deep Learning & AI Enthusiast
