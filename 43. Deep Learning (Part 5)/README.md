## Dataset

Download CIFAR-10 from:
https://www.cs.toronto.edu/~kriz/cifar.html

---

# ✅ Module Review: AI/ML Batch — Deep Learning & NLP

From the screenshots, this module covers:

## 🔹 Deep Learning (Part 5)

### CNN Section

✔ CNN for Image Classification
✔ Training the CNN
✔ CNN Code implementation
✔ Popular CNN Architecturess

### NLP & Sequence Models

✔ Natural Language Processing (NLP)
✔ Text Processing Techniques
✔ Advanced Text Processing
✔ Word2Vec
✔ TF-IDF
✔ RNN Architecture
✔ Types of RNNs
✔ Backpropagation in RNN
✔ LSTM Network & Architecture

👉 This is a **complete pipeline**:
**Computer Vision → NLP → Sequence Models**

---

# 🧠 CNN Project Review (CIFAR-10 Image Classification)

## ✔ 1. Imports & Libraries

```python
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
from torchvision.datasets import CIFAR10
from torch.utils.data import DataLoader
import torchvision.transforms as tran
```

### ✅ What this does:

- Loads PyTorch framework
- CIFAR-10 dataset loader
- DataLoader for batching
- Transforms for preprocessing

### ⚠ Issue

You imported transforms as:

```python
import torchvision.transforms as tran
```

But later used:

```python
transforms.Compose(...)
```

✔ Fix:

```python
import torchvision.transforms as transforms
```

---

## ✔ 2. Image Preprocessing

```python
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5))
])
```

### ✅ Purpose

- Convert image → tensor
- Normalize pixel values from **[0,1] → [-1,1]**
- Improves training stability

---

## ✔ 3. Loading Dataset

```python
train_dataset = CIFAR10(root="./data", train=True, download=True, transform=transform)
testing_dataset = CIFAR10(root="./data", train=False, download=True, transform=transform)
```

### ✅ Correct

- 50,000 training images
- 10,000 test images
- 10 classes (airplane, car, bird, cat…)

---

## ⚠ 4. DataLoader Bug

```python
train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(train_dataset, batch_size=64)
```

### ❌ Problem:

You used **train_dataset** again for testing.

### ✔ Fix:

```python
test_loader = DataLoader(testing_dataset, batch_size=64, shuffle=False)
```

---

## ❗ 5. CNN Model Definition (Incomplete)

Your notebook stops mid-definition:

```python
self.conv_layers = nn.Sequential(
    nn.Conv2d(3, 32, kernel_size=3, padding=1),
    nn.ReLU
```

### ❌ Issues:

- `nn.ReLU` missing parentheses → `nn.ReLU()`
- model incomplete
- no pooling
- no fully connected layers
- no forward function

---

## ✔ Correct CNN Architecture (Recommended)

Here is a **complete working version**:

```python
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()

        self.conv_layers = nn.Sequential(
            nn.Conv2d(3,32,3,padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2,2),

            nn.Conv2d(32,64,3,padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2,2)
        )

        self.fc_layers = nn.Sequential(
            nn.Linear(64*8*8, 512),
            nn.ReLU(),
            nn.Linear(512,10)
        )

    def forward(self,x):
        x = self.conv_layers(x)
        x = x.view(x.size(0), -1)
        x = self.fc_layers(x)
        return x
```

---

## ✔ 6. Loss & Optimizer

```python
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters())
```

### ✅ Correct choice:

- CrossEntropy → classification
- Adam → fast convergence

---

## ⚠ 7. Training Loop Issues

Your code:

```python
output = model.forward(images)
```

### ❌ Problems:

- Should call model directly
- typo: forword propagatio
- missing loss calculation
- missing backward pass
- missing optimizer step

---

## ✔ Correct Training Loop

```python
epochs = 10

for epoch in range(epochs):
    running_loss = 0

    for images, labels in train_loader:

        optimizer.zero_grad()

        outputs = model(images)
        loss = criterion(outputs, labels)

        loss.backward()
        optimizer.step()

        running_loss += loss.item()

    print(f"Epoch {epoch+1}, Loss: {running_loss/len(train_loader):.4f}")
```

---

## ✔ 8. Evaluation Code

Your evaluation started correctly:

```python
model.eval()
with torch.no_grad():
```

### ✔ Complete Version:

```python
correct = 0
total = 0

model.eval()

with torch.no_grad():
    for images, labels in test_loader:
        outputs = model(images)
        _, predicted = torch.max(outputs,1)

        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print("Accuracy:", 100 * correct / total)
```

---

# 🧠 CNN Concepts You Learned

## ✔ Convolution Layer

Detects edges, textures, shapes

## ✔ Pooling Layer

Reduces image size & computation

## ✔ Feature Maps

Represent learned visual patterns

## ✔ Fully Connected Layer

Performs classification

---

# 🧠 Popular CNN Architectures (from module)

You likely covered:

- LeNet
- AlexNet
- VGG
- ResNet
- Inception

👉 Used in:

- face recognition
- medical imaging
- self-driving cars
- security systems

---

# 🧠 NLP & Text Processing Section Review

## ✔ Text Processing Techniques

- Tokenization
- Stopword removal
- Stemming
- Lemmatization

## ✔ TF-IDF

Measures word importance.

TF = term frequency
IDF = rarity across documents

Used in:

- search engines
- document ranking
- spam filtering

---

## ✔ Word2Vec

Converts words → vectors.

Captures semantic meaning:

```
King - Man + Woman ≈ Queen
```

---

# 🧠 RNN & LSTM Section Review

## ✔ RNN

Processes sequential data:

- text
- speech
- time series

### Problem:

❌ Vanishing gradients
❌ short memory

---

## ✔ LSTM (Long Short-Term Memory)

Fixes RNN limitations.

### Gates:

- Forget gate
- Input gate
- Output gate

Used in:

- translation
- speech recognition
- chatbots
- stock prediction

---

# ⭐ Overall Evaluation of Your Module Learning

### ✅ Strong Coverage:

✔ CNN & image classification
✔ Dataset handling & training
✔ NLP fundamentals
✔ Word embeddings
✔ Sequential models (RNN & LSTM)

### ⚠ Needs Improvement:

🔹 Complete CNN architecture
🔹 Fix DataLoader bug
🔹 Proper training loop
🔹 Improve evaluation & accuracy tracking

---

# 🚀 Suggested Next Improvements

## 🔹 CNN Project Enhancements

✅ Add dropout to reduce overfitting
✅ Use GPU training
✅ Plot loss & accuracy graphs
✅ Try data augmentation

---

## 🔹 Practice Ideas

✔ Build cat vs dog classifier
✔ Train CNN on custom images
✔ Build sentiment analysis using LSTM
✔ Compare TF-IDF vs Word2Vec

---

# CNN-Based Image Classification on CIFAR-10

## 📌 Project Overview

This project implements a **Convolutional Neural Network (CNN)** using PyTorch to perform image classification on the **CIFAR-10 dataset**. The objective is to design, train, and evaluate a deep learning model capable of accurately classifying images into one of ten object categories.

This project was completed as part of a **Deep Learning & AI/ML coursework module**, demonstrating practical understanding of convolutional neural networks and model training workflows.

---

## 🎯 Objectives

- Understand and implement CNN architecture for image classification
- Apply preprocessing and normalization techniques
- Train and evaluate a deep learning model
- Analyze performance and accuracy metrics
- Gain hands-on experience with PyTorch and computer vision workflows

---

## 🧠 Dataset: CIFAR-10

The CIFAR-10 dataset is a widely used benchmark dataset for image classification.

**Dataset Details:**

- 60,000 color images (32×32 pixels)
- 10 classes
- 50,000 training images
- 10,000 testing images

**Classes:**

- Airplane
- Automobile
- Bird
- Cat
- Deer
- Dog
- Frog
- Horse
- Ship
- Truck

Source: [https://www.cs.toronto.edu/~kriz/cifar.html](https://www.cs.toronto.edu/~kriz/cifar.html)

---

## 🏗️ Model Architecture

The CNN model consists of the following components:

### Convolutional Layers

- Conv2D (3 → 32 filters, 3×3 kernel)
- ReLU Activation
- MaxPooling (2×2)
- Conv2D (32 → 64 filters, 3×3 kernel)
- ReLU Activation
- MaxPooling (2×2)

### Fully Connected Layers

- Flatten Layer
- Dense Layer (512 neurons, ReLU)
- Output Layer (10 classes)

---

## ⚙️ Technologies & Libraries

- Python
- PyTorch
- Torchvision
- NumPy
- Matplotlib (optional for visualization)

---

## 🔄 Workflow

### 1️⃣ Data Preprocessing

- Convert images to tensors
- Normalize pixel values

### 2️⃣ Data Loading

- Load CIFAR-10 dataset
- Create training and testing loaders

### 3️⃣ Model Training

- Loss Function: CrossEntropyLoss
- Optimizer: Adam
- Backpropagation and gradient updates

### 4️⃣ Model Evaluation

- Compute classification accuracy
- Evaluate performance on unseen test data

---

## 📊 Results

Typical performance after training:

- Training Accuracy: ~70–85%
- Testing Accuracy: ~65–75%

_(Results may vary depending on training epochs and hyperparameters.)_

---

## ▶️ How to Run the Project

### 1. Install Dependencies

```bash
pip install torch torchvision
```

### 2. Run the Notebook

Open and run:

```
CNN_for_CIFAR10.ipynb
```

### 3. Train the Model

Execute all cells to:

- download dataset
- train CNN
- evaluate accuracy

---

## 📈 Possible Improvements

- Add data augmentation
- Implement dropout to reduce overfitting
- Train on GPU for faster performance
- Experiment with deeper architectures
- Compare with ResNet or VGG models

---

## 📚 Learning Outcomes

Through this project, the following concepts were reinforced:

- Convolutional Neural Networks
- Image preprocessing & normalization
- Model training & optimization
- Performance evaluation
- Deep learning workflow implementation

---

## 🔮 Future Work

- Extend to custom image datasets
- Deploy model as a web application
- Implement real-time object detection
- Compare CNN with transfer learning models

---

## 👨‍🎓 Academic Context

This project was developed as part of an academic module on **Deep Learning and Artificial Intelligence**, focusing on practical implementation of CNNs for image classification tasks.

---

## 📜 License

This project is intended for **educational and research purposes**.

---

## 🙏 Acknowledgements

- CIFAR-10 Dataset by University of Toronto
- PyTorch Deep Learning Framework
- Course instructors and academic resources

---

**Author:** Satinder Singh Sall
**Program:** AI/ML Coursework Module
**Focus Area:** Deep Learning & Computer Vision
