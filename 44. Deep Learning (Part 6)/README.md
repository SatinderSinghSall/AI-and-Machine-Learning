# AI / ML: Deep Learning – Part 6

## Sentiment Analysis using RNN

This section contains code and notes for building an **RNN-based sentiment analysis model** using the IMDB dataset.

### Dataset

The dataset used in this project is **IMDB Movie Reviews Dataset**.

Due to GitHub file size limitations, the dataset is **not included in this repository**.

You can download it from:

https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews

After downloading, place the file in:

```
44. Deep Learning (Part 6)/Lecture Dataset/
```

Expected filename:

```
IMDB Dataset.csv
```

I carefully reviewed both screenshots from **start to finish** and analyzed all visible items in the module sidebar and the dataset/code context shown in the video. Below is a **complete breakdown of what you learned in this module** and what each part means technically.

---

# Module Review: **Deep Learning (Part 6) – RNN for Sentiment Analysis**

This module walks through **building a sentiment analysis model using RNN** on a text dataset (IMDB movie reviews).

The pipeline follows the **standard NLP deep learning workflow**:

```
Dataset → Text Cleaning → Token Processing → Vectorization → RNN Model → Training → Evaluation
```

---

# 1️⃣ Dataset: IMDB Movie Reviews

From the screenshot:

File used:

```
IMDB Dataset.csv
```

Columns visible:

```
review | sentiment
```

Example rows:

```
"Watching Oz, you may become comfortable..."
sentiment: positive

"some meaningless thriller spots..."
sentiment: negative
```

### What this dataset contains

- Movie reviews written by users
- Labels:
  - **positive**
  - **negative**

### Goal

Predict sentiment using a **Recurrent Neural Network (RNN)**.

So the problem type is:

```
Supervised Learning
Binary Text Classification
```

---

# 2️⃣ Text Preprocessing with Regex

You learned to clean raw text using **regular expressions**.

Typical operations:

Remove:

```
HTML tags
special characters
punctuation
numbers
extra spaces
```

Example transformation:

```
Original:
"I loved this movie!!! <br/>"

Cleaned:
"i loved this movie"
```

Example code usually used:

```python
import re

def clean_text(text):
    text = re.sub(r'<.*?>', '', text)   # remove HTML tags
    text = re.sub(r'[^a-zA-Z]', ' ', text)  # keep only letters
    text = text.lower()
    return text
```

---

# 3️⃣ Removing Stopwords (NLTK)

You learned how to remove **common words that add little meaning**.

Examples:

```
the
is
was
are
and
of
```

Using **NLTK**.

Typical code:

```python
from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))

filtered_words = [word for word in words if word not in stop_words]
```

Example:

```
Original:
"This movie was really very good"

After stopword removal:
"movie really good"
```

---

# 4️⃣ Stemming

You learned **stemming** to reduce words to root forms.

Example:

```
running → run
played → play
movies → movie
```

Typical algorithm used:

```
PorterStemmer
```

Example code:

```python
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in words]
```

Example result:

```
loved → love
watching → watch
movies → movi
```

---

# 5️⃣ TF-IDF Vectorization

You converted text into **numerical vectors**.

Machine learning models **cannot read text**, so we convert words to numbers.

TF-IDF measures:

```
Term Frequency × Inverse Document Frequency
```

Meaning:

```
Importance of word in document
```

Example:

```
review = "movie was good"

Vector:

movie : 0.45
good  : 0.76
bad   : 0
```

Typical code:

```python
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(corpus)
```

---

# 6️⃣ DataLoaders

The module then moved to **deep learning pipeline using PyTorch DataLoaders**.

Purpose:

```
Efficiently feed batches of data to the neural network.
```

Instead of sending all data at once:

```
Batch training
```

Example:

```python
from torch.utils.data import DataLoader, Dataset
```

Typical pipeline:

```
Dataset → DataLoader → Model → Training loop
```

Benefits:

- faster training
- memory efficient
- supports GPU training

---

# 7️⃣ Building the RNN Model

You built a **Recurrent Neural Network for text sequences**.

RNN processes text **word by word in sequence**.

Example sentence:

```
"This movie was very good"
```

RNN reads:

```
This → movie → was → very → good
```

And remembers context.

Typical architecture:

```
Embedding Layer
        ↓
RNN Layer
        ↓
Fully Connected Layer
        ↓
Sigmoid Output
```

Example PyTorch style:

```python
import torch.nn as nn

class RNNModel(nn.Module):
    def __init__(self):
        super().__init__()

        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.rnn = nn.RNN(embedding_dim, hidden_dim)
        self.fc = nn.Linear(hidden_dim, 1)

    def forward(self, x):
        x = self.embedding(x)
        out, hidden = self.rnn(x)
        out = self.fc(hidden.squeeze(0))
        return out
```

---

# 8️⃣ Training the Model

Training steps learned:

1️⃣ Forward pass

```
prediction = model(x)
```

2️⃣ Compute loss

```
loss = criterion(prediction, y)
```

3️⃣ Backpropagation

```
loss.backward()
```

4️⃣ Update weights

```
optimizer.step()
```

Typical training loop:

```python
for epoch in range(epochs):

    for x_batch, y_batch in train_loader:

        optimizer.zero_grad()

        output = model(x_batch)

        loss = criterion(output, y_batch)

        loss.backward()

        optimizer.step()
```

---

# 9️⃣ Model Evaluation

You then evaluated performance.

Metrics used for sentiment analysis typically:

```
Accuracy
Precision
Recall
F1 Score
```

Example:

```
Accuracy = 88%
```

Meaning:

```
88% predictions correct
```

---

# 🔟 Final Output Example

Input review:

```
"This movie was absolutely fantastic"
```

Model prediction:

```
Positive
```

Another:

```
"This film was boring and terrible"
```

Prediction:

```
Negative
```

---

# 🧠 Full Pipeline You Learned

Your module teaches this complete NLP deep learning workflow:

```
IMDB Dataset
     ↓
Text Cleaning (Regex)
     ↓
Stopword Removal (NLTK)
     ↓
Stemming
     ↓
TF-IDF Vectorization
     ↓
Dataset + DataLoader
     ↓
RNN Model
     ↓
Training Loop
     ↓
Evaluation
     ↓
Sentiment Prediction
```

---

# 📚 Additional Items in Sidebar

I also noted these files in the module:

### 📄 RNN Code

Contains the full notebook or implementation.

### 📄 Handwritten Digit Classification Assignment

Another deep learning task (likely CNN on MNIST).

### 📄 Refer for MNIST Dataset

Resource explaining the dataset.

---

# ⭐ What You Achieved in This Module

After finishing this module you now understand:

✔ Text preprocessing
✔ Regex cleaning
✔ NLTK stopwords
✔ Stemming
✔ TF-IDF vectorization
✔ PyTorch DataLoaders
✔ Building RNN models
✔ Training neural networks
✔ Sentiment analysis

This is a **complete beginner-to-intermediate NLP pipeline**.

---
