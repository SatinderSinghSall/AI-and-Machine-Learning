# 📘 Module Review: Deep Learning (ANN)

## 🎯 Core Concept Covered

You learned how to build **Artificial Neural Networks (ANNs)** using **PyTorch** for:

✔ Regression problems
✔ Classification problems
✔ Model training & evaluation
✔ Data preprocessing & pipelines

---

# 🧠 ANN for Regression (Power Plant Dataset)

## 📊 Problem

Predict **energy output (PE)** of a power plant.

### Features:

- **AT** → Temperature
- **VT** → Vacuum
- **AP** → Pressure
- **RH** → Humdity

### Target:

- **PE** → Energy Output

This is a **continuous value → regression problem**.

---

## 🔄 Complete Pipeline You Implemented

### ✅ 1️⃣ Load & Inspect Data

```python
df = pd.read_csv("powerplant_data.csv")
df.isnull().sum()
```

✔ Good practice checking missing values.

---

### ✅ 2️⃣ Split Features & Labels

```python
X = df.drop("PE", axis=1)
y = df["PE"]
```

---

### ✅ 3️⃣ Train/Test Split

```python
train_test_split(..., test_size=0.2, random_state=42)
```

✔ Ensures reproducibility.

---

### ✅ 4️⃣ Feature Scaling

```python
StandardScaler()
```

✔ VERY IMPORTANT for neural networks.

Without scaling → slow training & poor convergence.

---

### ✅ 5️⃣ Convert to PyTorch Tensors

```python
torch.tensor(..., dtype=torch.float32)
```

✔ Regression targets reshaped:

```python
.view(-1,1)
```

Correct for output layer compatibility.

---

### ✅ 6️⃣ TensorDataset & DataLoader

You created mini-batches:

```python
train_loader = DataLoader(..., batch_size=32, shuffle=True)
```

✔ Enables:

- faster training
- gradient stability
- memory efficiency

---

## 🧠 ANN Model Architecture

```python
nn.Linear(4, 6)
ReLU
nn.Linear(6, 6)
ReLU
nn.Linear(6, 1)
```

### What this means:

Input (4 features)
→ Hidden layer (6 neurons)
→ Hidden layer (6 neurons)
→ Output (1 value)

✔ ReLU introduces non-linearity.

---

## ⚙ Loss & Optimizer

```python
nn.MSELoss()
optim.Adam()
```

✔ MSE → standard for regression
✔ Adam → adaptive learning optimizer

---

## 🔁 Training Loop

### Steps per batch:

✔ zero gradients
✔ forward pass
✔ compute loss
✔ backpropagation
✔ update weights

This is **core deep learning training logic**.

---

### ⚠️ IMPORTANT ERRORS TO FIX

You wrote:

```python
crietrion
crietian
```

But defined:

```python
criterion = nn.MSELoss()
```

✅ Must use consistent spelling.

---

### ⚠️ Validation Loss Issue

You used:

```python
running_val_loss += loss
```

Should be:

```python
running_val_loss += loss.item()
```

Otherwise tensor accumulation may cause issues.

---

## 💾 Saving Best Model

```python
torch.save(model.state_dict(), "best_model.pt")
```

✔ Saves only best weights → professional practice.

---

## 📉 Loss Curve Plot

You plotted training vs validation loss.

✔ Used to detect:

- overfitting
- underfitting
- convergence

---

## 📊 Evaluation Metrics

### MSE

```python
train_mse_loss
test_mse_loss
```

### R² Score

```python
r2_score()
```

✔ R² closer to 1 → better predictions.

---

## 📈 Prediction Comparison

You compared:

Predicted vs Actual values

✔ essential for regression evaluation.

---

# 🧠 ANN for Classification (Date Fruit Dataset)

## 📊 Problem

Classify date fruit type.

- 34 features
- 7 classes
- Multi-class classification

---

## 🔤 Label Encoding

```python
LabelEncoder()
```

Converts class names → integers.

✔ Required for neural networks.

---

## 🔄 Scaling Features

✔ Important because features likely have different ranges.

---

## 🧠 Model Architecture

```python
Input → 64 → 64 → 7 outputs
```

Output layer = **7 neurons**
(one per class)

---

## ❗ Why no Softmax?

Because you used:

```python
nn.CrossEntropyLoss()
```

CrossEntropyLoss automatically applies:

✔ Softmax
✔ Log likelihood

---

## 🎯 Training Logic

Same pipeline:
✔ forward pass
✔ loss
✔ backpropagation
✔ optimizer step

---

## 📊 Prediction Logic

```python
_, predicted = torch.max(outputs, 1)
```

Selects class with highest probability.

---

## 📈 Accuracy Calculation

```python
accuracy = correct / total
```

✔ Standard classification metric.

---

# 📚 Concepts You Mastered

## 🔹 Neural Network Workflow

✔ preprocessing
✔ tensor conversion
✔ batching
✔ model creation
✔ training loop
✔ validation
✔ saving best model
✔ evaluation

---

## 🔹 Regression vs Classification

| Task           | Output      | Loss         | Metric   |
| -------------- | ----------- | ------------ | -------- |
| Regression     | continuous  | MSE          | R², RMSE |
| Classification | class index | CrossEntropy | Accuracy |

---

## 🔹 Why Scaling Matters

Neural networks converge faster with normalized inputs.

---

## 🔹 Why DataLoader Matters

Efficient training & gradient stability.

---

## 🔹 Why Save Best Model

Prevents using overfitted weights.

---

# 📷 Topics Seen in Course Panel (Upcoming / Covered)

### Deep Learning (Part 3)

✔ ANN Regression
✔ Dataset loading
✔ Training & evaluation

### Deep Learning (Part 4)

You are moving toward:

- Feedforward networks (FNN)
- Computer Vision
- CNN necessity
- CNN architecture
- Convolution layers
- Pooling layers
- Fully connected layers

👉 This means you’re transitioning from **tabular deep learning → image deep learning**.

---

# 🧠 Professional-Level Improvements

## ✔ Add Early Stopping

Stop when validation loss stops improving.

## ✔ Add Learning Rate

```python
optim.Adam(model.parameters(), lr=0.001)
```

## ✔ Add Dropout (prevent overfitting)

```python
nn.Dropout(0.2)
```

## ✔ Try deeper networks

## ✔ Try different batch sizes

---

# ⭐ What You Now Understand (BIG PICTURE)

You can now:

✅ Build neural networks from scratch
✅ Train regression & classification models
✅ Prepare data for deep learning
✅ Evaluate model performance
✅ Save & reload trained models

👉 This is the **foundation of deep learning engineering.**

---

# Artificial Neural Networks for Regression & Classification

## 📌 Overview

This project demonstrates the implementation of **Artificial Neural Networks (ANNs)** using **PyTorch** for solving both regression and classification problems. It follows a complete deep learning workflow including data preprocessing, model building, training, evaluation, and model saving.

The work is based on real-world datasets and reflects practical machine learning engineering practices.

---

## 🎯 Objectives

- Build ANN models from scratch using PyTorch
- Apply neural networks to regression and classification tasks
- Implement efficient data pipelines using DataLoader
- Evaluate model performance using appropriate metrics
- Save and reload the best-performing model

---

## 🧠 Projects Included

### 1️⃣ ANN for Regression

**Dataset:** Power Plant Energy Output

**Goal:** Predict electrical energy output (PE) based on environmental conditions.

**Input Features:**

- Temperature (AT)
- Exhaust Vacuum (VT)
- Ambient Pressure (AP)
- Relative Humdity (RH)

**Target Variable:**

- Energy Output (PE)

**Techniques Used:**

- Feature scaling (StandardScaler)
- TensorDataset & DataLoader
- Feedforward Neural Network
- MSE Loss & Adam Optimizer
- Model checkpointing
- R² score & MSE evaluation

---

### 2️⃣ ANN for Classification

**Dataset:** Date Fruit Classification

**Goal:** Classify date fruit samples into one of seven classes using physical and chemical features.

**Dataset Characteristics:**

- 34 input features
- 7 target classes

**Techniques Used:**

- Label Encoding
- Feature scaling
- Multi-class neural network
- CrossEntropyLoss
- Accuracy evaluation

---

## 🏗 Project Structure

```
├── ANN-Regression-Algo.ipynb
├── ANN_Classification.ipynb
├── powerplant_data.csv
├── DateFruit_Dataset.csv
├── best_model.pt
└── README.md
```

---

## ⚙️ Installation & Requirements

### 🔹 Dependencies

- Python 3.x
- PyTorch
- NumPy
- Pandas
- Scikit-learn
- Matplotlib

### 🔹 Install Required Packages

```bash
pip install torch pandas numpy scikit-learn matplotlib
```

---

## 🚀 Workflow

### 1. Data Preparation

- Load datasets
- Handle missing values
- Normalize features
- Train-test split

### 2. Tensor Conversion

- Convert data into PyTorch tensors
- Create TensorDataset
- Load batches using DataLoader

### 3. Model Architecture

- Fully connected feedforward neural network
- ReLU activation functions

### 4. Training Process

- Forward propagation
- Loss computation
- Backpropagation
- Weight updates using Adam optimizer

### 5. Model Evaluation

- Regression: MSE, R² Score
- Classification: Accuracy
- Prediction vs Actual comparison

### 6. Model Saving

- Best model saved based on validation loss

---

## 📊 Results & Evaluation

### Regression Model

- Successfully predicts power plant energy output
- Performance evaluated using MSE and R² score

### Classification Model

- Accurately classifies date fruit varieties
- Performance evaluated using classification accuracy

---

## 📈 Key Concepts Demonstrated

- Artificial Neural Networks (ANN)
- Regression vs Classification modeling
- Feature scaling importance
- Mini-batch training
- Model evaluation metrics
- Overfitting prevention via validation monitoring
- Model checkpointing

---

## 🧩 Future Improvements

- Implement Early Stopping
- Add Dropout layers for regularization
- Hyperparameter tuning
- Experiment with deeper architectures
- Deploy model using Flask or FastAPI
- Extend to CNNs for image-based tasks

---

## 🎓 Academic Relevance

This project demonstrates:

- Understanding of deep learning fundamentals
- Practical implementation of neural networks
- Knowledge of PyTorch training pipelines
- Data preprocessing & evaluation techniques

Suitable for coursework, research demonstrations, and academic submissions.

---

## 👨‍💻 Author

**Satinder Singh Sall**
AI/ML Enthusiast & Deep Learning Practitioner

---

## 📜 License

This project is intended for educational and research purposes.

# 🧠 COMPLETE LEARNING SUMMARY

##_toggle_This module taught you how to build, train, evaluate, and deploy Artificial Neural Networks using PyTorch._

---

# 🎓 1. FOUNDATIONS OF NEURAL NETWORKS

## ✅ What an ANN is

You learned:

✔ ANN = computational model inspired by the human brain
✔ neurons → layers → network
✔ learns patterns via weight updates

### ANN Structure:

- Input layer
- Hidden layers
- Output layer

---

## ✅ Why Neural Networks are Powerful

You learned they can:

✔ learn nonlinear relationships
✔ model complex data patterns
✔ outperform linear models on complex tasks

---

# 🧠 2. REGRESSION vs CLASSIFICATION

## ✅ Regression

Used when output is continuous.

✔ Example: energy output prediction
✔ Output = single numeric value
✔ Loss = Mean Squared Error

---

## ✅ Classification

Used when output is categories.

✔ Example: fruit type prediction
✔ Output = class index
✔ Loss = CrossEntropyLoss

---

# 📊 3. DATA PREPROCESSING & PREPARATION

## ✅ Loading Data

You used:

✔ Pandas to load CSV files
✔ `.head()` & `.info()` to inspect data
✔ `.isnull().sum()` to check missing values

---

## ✅ Feature & Target Separation

### Regression:

```python
X = df.drop("PE", axis=1)
y = df["PE"]
```

### Classification:

```python
X = df.drop("Class", axis=1)
y = df["Class"]
```

---

## ✅ Train-Test Split

You learned:

✔ importance of unseen data evaluation
✔ reproducibility with `random_state`

---

## ✅ Feature Scaling (VERY IMPORTANT)

You used:

✔ `StandardScaler()`

### Why scaling matters:

✔ neural networks converge faster
✔ prevents large features dominating learning
✔ improves stability

---

## 🧠 4. LABEL ENCODING (CLASSIFICATION)

You learned:

✔ neural networks require numeric labels
✔ LabelEncoder converts categories → integers

---

# 🔢 5. CONVERTING DATA TO PYTORCH TENSORS

You learned:

✔ neural networks use tensors (not NumPy arrays)
✔ use `torch.tensor()`
✔ regression target reshaped using `.view(-1,1)`

---

# ⚙️ 6. TENSORDATASET & DATALOADER

## ✅ TensorDataset

Wraps inputs & labels together.

## ✅ DataLoader

Creates mini-batches.

### Why DataLoader is important:

✔ memory efficiency
✔ faster training
✔ stable gradients
✔ shuffling prevents bias

---

# 🧠 7. BUILDING ANN MODELS

## ✅ Defining Neural Network Class

You learned:

✔ subclass `nn.Module`
✔ define layers in `__init__()`
✔ define forward pass in `forward()`

---

## ✅ Linear Layers

```python
nn.Linear(input, output)
```

Represents:

✔ weights + bias
✔ mathematical transformation

---

## ✅ Activation Functions

You used:

✔ ReLU (Rectified Linear Unit)

### Why ReLU:

✔ introduces non-linearity
✔ prevents vanishing gradient
✔ faster training

---

# 🧠 8. MODEL ARCHITECTURE DESIGN

## Regression Model

Input → 6 → 6 → Output(1)

## Classification Model

Input → 64 → 64 → Output(7 classes)

You learned:

✔ hidden layers learn patterns
✔ deeper layers learn complex features
✔ output layer depends on task

---

# ⚙️ 9. LOSS FUNCTIONS

## Regression:

### Mean Squared Error (MSE)

Measures prediction error.

---

## Classification:

### CrossEntropyLoss

Combines:

✔ Softmax
✔ Log Loss

Used for multi-class classification.

---

# ⚙️ 10. OPTIMIZER (LEARNING)

You used:

✔ Adam optimizer

### Why Adam:

✔ adaptive learning rate
✔ fast convergence
✔ widely used in deep learning

---

# 🔁 11. TRAINING LOOP (CORE OF DEEP LEARNING)

You learned the **standard training workflow**:

### Step-by-step:

1️⃣ zero gradients
2️⃣ forward pass
3️⃣ compute loss
4️⃣ backpropagation
5️⃣ optimizer step

This is the heart of neural network learning.

---

# 🔁 12. BACKPROPAGATION

You learned:

✔ gradients compute error contribution
✔ weights updated to reduce loss
✔ network learns patterns iteratively

---

# 📉 13. VALIDATION DURING TRAINING

You implemented:

✔ validation loss tracking
✔ evaluation mode (`model.eval()`)
✔ disabling gradients (`torch.no_grad()`)

### Why validation:

✔ detect overfitting
✔ monitor generalization

---

# 💾 14. MODEL CHECKPOINTING

You saved best model using:

```python
torch.save(model.state_dict(), "best_model.pt")
```

### Why this matters:

✔ saves best weights
✔ prevents overfitting issues
✔ professional practice

---

# 📊 15. LOSS CURVE ANALYSIS

You plotted:

✔ training loss
✔ validation loss

### Used to detect:

✔ overfitting
✔ underfitting
✔ convergence

---

# 📊 16. MODEL EVALUATION

## Regression Metrics

### ✔ Mean Squared Error (MSE)

Measures average squared prediction error.

### ✔ R² Score

Measures prediction quality (closer to 1 is better).

---

## Classification Metrics

### ✔ Accuracy

Percentage of correct predictions.

---

# 🔍 17. PREDICTION LOGIC

## Regression

Predicted values compared with actual values.

## Classification

```python
_, predicted = torch.max(outputs, 1)
```

Select class with highest probability.

---

# 🧠 18. PRACTICAL ML ENGINEERING SKILLS

You learned:

✔ batching data
✔ efficient training pipelines
✔ separating training & validation logic
✔ saving models
✔ evaluating performance
✔ comparing predictions

---

# 📚 19. COURSE TOPICS COVERED (FROM SCREENSHOTS)

### Deep Learning (Part 3)

✔ ANN for Regression
✔ Data loading & tensors
✔ TensorDataset & DataLoader
✔ Building ANN
✔ Training ANN
✔ Saving & loading model
✔ Evaluation

---

### Deep Learning (Part 4) — Upcoming Topics

You are transitioning toward:

✔ Feedforward Network architectures
✔ Computer Vision
✔ Why CNNs are needed
✔ CNN architecture
✔ Convolution layers
✔ Pooling layers
✔ Fully connected layers

👉 This moves you from **tabular data → image deep learning**.

---

# 🏆 BIG PICTURE: WHAT YOU CAN DO NOW

You can now:

✅ build ANN models from scratch
✅ solve regression & classification problems
✅ preprocess data for deep learning
✅ train models efficiently using PyTorch
✅ evaluate & improve model performance
✅ save & reload trained models

👉 These are **core skills of a deep learning engineer.**

---
