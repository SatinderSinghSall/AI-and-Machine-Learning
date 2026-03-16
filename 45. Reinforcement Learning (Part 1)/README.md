# AI / ML: Deep Learning – Part 6

# Deep Learning & Reinforcement Learning Module

## Overview

This repository documents the concepts, experiments, and implementation completed during the AI/ML module focusing on **Recurrent Neural Networks (RNN) for Sentiment Analysis** and **Fundamentals of Reinforcement Learning (RL)**.

The project demonstrates the complete machine learning pipeline including:

- Natural Language Processing (NLP)
- Text preprocessing
- Feature engineering
- Deep learning model development
- Model training and evaluation
- Reinforcement Learning concepts and grid-world example

---

# Table of Contents

1. Introduction
2. Dataset
3. NLP Preprocessing Pipeline
4. Text Vectorization
5. Data Loading with PyTorch
6. RNN Architecture
7. Model Training
8. Model Evaluation
9. Reinforcement Learning Concepts
10. Markov Decision Process (MDP)
11. Grid World Environment
12. Policy and Value Functions
13. Q-Functions
14. Exploration vs Exploitation
15. Skills Acquired
16. Future Improvements
17. Technologies Used

---

# 1. Introduction

Sentiment Analysis is a Natural Language Processing task that aims to determine the sentiment expressed in a piece of text.

The objective of this project is to build a deep learning model using **Recurrent Neural Networks (RNNs)** to classify movie reviews as either:

- Positive
- Negative

The project follows the standard NLP pipeline including preprocessing, tokenization, numerical encoding, and training an RNN model using PyTorch.

Additionally, the module introduces core **Reinforcement Learning (RL)** concepts such as Markov Decision Processes, policies, Q-functions, and exploration strategies.

---

# 2. Dataset

The dataset used in this project is the **IMDB Movie Reviews Dataset**.

Dataset structure:

| Column    | Description               |
| --------- | ------------------------- |
| review    | Movie review text         |
| sentiment | positive / negative label |

Example record:

```
review: "Watching Oz, you may become comfortable with what is uncomfortable viewing"
sentiment: positive
```

Goal:

```
Input: Movie review text
Output: Sentiment classification (Positive / Negative)
```

This is a **Binary Text Classification problem**.

---

# 3. NLP Preprocessing Pipeline

Text data cannot be directly used by machine learning models. It must be cleaned and transformed into a structured format.

The preprocessing steps implemented include:

1. Regex text cleaning
2. Lowercasing
3. Stopword removal
4. Stemming

---

## 3.1 Regex Cleaning

Regular Expressions (Regex) are used to remove unwanted characters such as punctuation, numbers, and special symbols.

Example implementation:

```python
import re

text = re.sub(r'[^a-zA-Z]', ' ', text)
text = text.lower()
```

Example:

```
Original:
"I loved this movie!!! 10/10"

After Regex:
"i loved this movie"
```

---

## 3.2 Stopword Removal

Stopwords are common words that do not carry significant meaning for classification.

Examples:

```
the
is
was
and
in
on
```

Implementation using NLTK:

```python
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))
words = [w for w in text.split() if w not in stop_words]
```

Example:

```
Original:
"this movie was very good"

After stopword removal:
"movie good"
```

---

## 3.3 Stemming

Stemming reduces words to their root form.

Examples:

| Word    | Stem |
| ------- | ---- |
| playing | play |
| played  | play |
| movies  | movi |

Implementation:

```python
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
word = stemmer.stem(word)
```

Purpose:

- Reduce vocabulary size
- Improve generalization

---

# 4. Text Vectorization

Machine learning models require numerical inputs. Text must therefore be converted into numerical representations.

Two approaches discussed in this module include:

- TF-IDF
- Tokenization with embeddings

---

## 4.1 TF-IDF

TF-IDF (Term Frequency–Inverse Document Frequency) measures the importance of words in a document relative to a corpus.

Concept:

```
TF = Term Frequency
IDF = Inverse Document Frequency

TF-IDF = TF × IDF
```

Example vector representation:

```
"movie good acting"

[0.12, 0.75, 0.45]
```

---

## 4.2 Tokenization

Tokenization converts words into integer indices.

Example vocabulary:

```
movie → 1
good → 2
bad → 3
acting → 4
```

Sentence:

```
"good movie"
```

Tokenized output:

```
[2, 1]
```

---

## 4.3 Padding

Deep learning models require fixed-length sequences.

Example:

Before padding:

```
[2,1]
[4,1,2,3]
```

After padding:

```
[0,0,2,1]
[4,1,2,3]
```

---

# 5. Data Loading with PyTorch

PyTorch provides **DataLoader** for efficient training.

Benefits:

- Batch processing
- Dataset shuffling
- Efficient memory usage

Example:

```python
train_loader = DataLoader(dataset,
                          batch_size=32,
                          shuffle=True)
```

Pipeline:

```
Dataset
 ↓
TensorDataset
 ↓
DataLoader
 ↓
Training Loop
```

---

# 6. RNN Architecture

Recurrent Neural Networks are designed for sequential data such as text.

Model architecture:

```
Input Tokens
     ↓
Embedding Layer
     ↓
RNN Layer
     ↓
Hidden State
     ↓
Fully Connected Layer
     ↓
Sigmoid Activation
     ↓
Sentiment Prediction
```

Example PyTorch implementation:

```python
class SentimentRNN(nn.Module):

    def __init__(self):
        super().__init__()

        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.rnn = nn.RNN(embedding_dim, hidden_dim)
        self.fc = nn.Linear(hidden_dim, 1)

    def forward(self, x):

        x = self.embedding(x)

        output, hidden = self.rnn(x)

        out = self.fc(hidden[-1])

        return torch.sigmoid(out)
```

---

# 7. Model Training

Training involves optimizing the model parameters to minimize prediction error.

Training loop:

```python
for batch in train_loader:

    optimizer.zero_grad()

    outputs = model(inputs)

    loss = criterion(outputs, labels)

    loss.backward()

    optimizer.step()
```

Loss function used:

```
Binary Cross Entropy (BCELoss)
```

---

# 8. Model Evaluation

Model performance is evaluated using accuracy and loss metrics.

Example result:

```
Accuracy: 87%
```

Meaning:

```
87% of reviews were correctly classified
```

---

# 9. Reinforcement Learning Concepts

Reinforcement Learning is a paradigm where an agent learns to make decisions by interacting with an environment.

Key components:

| Component   | Description                         |
| ----------- | ----------------------------------- |
| Agent       | Learner or decision maker           |
| Environment | The system the agent interacts with |
| Action      | Decision taken by the agent         |
| Reward      | Feedback from the environment       |

Objective:

```
Maximize cumulative reward
```

---

# 10. Markov Decision Process (MDP)

Reinforcement Learning problems are often modeled using a Markov Decision Process.

MDP definition:

```
(S, A, P, R, γ)
```

| Symbol | Meaning                      |
| ------ | ---------------------------- |
| S      | Set of states                |
| A      | Set of actions               |
| P      | State transition probability |
| R      | Reward function              |
| γ      | Discount factor              |

---

# 11. Grid World Environment

A common RL example is the Grid World environment.

Grid structure:

```
0 1 2 3
--------
| | | | |
| | |X| |
|S| |X|E|
```

Legend:

```
S → Start state
E → Goal / End state
X → Obstacle
```

Allowed actions:

```
Up
Down
Left
Right
```

Goal:

```
Find the optimal path from S to E
```

---

# 12. Policy

A policy defines the behavior of the agent.

Definition:

```
π(s) → action
```

Example:

```
π(S) = Right
π(state_1) = Up
```

---

# 13. Q-Functions

The Q-function estimates the expected reward of taking a specific action in a given state.

Definition:

```
Q(s,a) = expected future reward
```

Update rule:

```
Q(s,a) = r + γ max Q(s',a')
```

Applications:

- Q-Learning
- Deep Q Networks (DQN)

---

# 14. Exploration vs Exploitation

A critical trade-off in reinforcement learning.

| Strategy     | Description              |
| ------------ | ------------------------ |
| Exploration  | Trying new actions       |
| Exploitation | Using known best actions |

Example strategy:

```
ε-greedy
```

Example:

```
ε = 0.1

10% exploration
90% exploitation
```

---

# 15. Skills Acquired

This module provided experience in the following areas:

## Natural Language Processing

- Text preprocessing
- Regex cleaning
- Stopword removal
- Stemming
- Tokenization
- TF-IDF
- Sentiment analysis

## Deep Learning

- Recurrent Neural Networks
- Embedding layers
- PyTorch DataLoader
- Training loops
- Binary classification models

## Reinforcement Learning

- RL fundamentals
- Markov Decision Processes
- Grid-world environments
- Policy functions
- Q-functions
- Exploration strategies

---

# 16. Future Improvements

Potential improvements to extend this project include:

### Replace RNN with LSTM

RNNs suffer from the vanishing gradient problem.

Better alternatives:

- LSTM
- GRU

### Use Pretrained Embeddings

Examples:

- GloVe
- Word2Vec
- FastText

### Add Evaluation Metrics

Additional metrics:

- Precision
- Recall
- F1 Score
- Confusion Matrix

### Try Transformer Models

Modern NLP models include:

- BERT
- RoBERTa
- GPT

---

# 17. Technologies Used

Programming Language:

- Python

Libraries:

- PyTorch
- NLTK
- NumPy
- Pandas
- Scikit-learn

Tools:

- Jupyter Notebook
- VS Code

---

# Conclusion

This project demonstrates the complete workflow for building a deep learning NLP model for sentiment classification and introduces key Reinforcement Learning concepts.

The combination of NLP preprocessing, RNN architecture, and RL fundamentals provides a strong foundation for advanced machine learning applications.
