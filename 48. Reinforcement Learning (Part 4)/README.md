# AI / ML: Deep Learning – Reinforcement Learning (Part 3 & 4)

# Reinforcement Learning & Deep Reinforcement Learning — Comprehensive Study

# 🐦 Deep Q-Network (DQN) for Flappy Bird

This project implements a **Deep Reinforcement Learning (DRL)** agent using **Deep Q-Networks (DQN)** to learn how to play the Flappy Bird game.

The agent is trained using **Gymnasium’s FlappyBird-v0 environment** and leverages core reinforcement learning techniques such as:

- Experience Replay
- Target Networks
- Epsilon-Greedy Exploration
- Neural Network Function Approximation

---

## 📚 Concepts Covered

This project demonstrates the practical implementation of:

- Reinforcement Learning fundamentals
- Q-Learning and Bellman Equation
- Deep Q-Networks (DQN)
- Experience Replay Buffer
- Policy Network vs Target Network
- Epsilon-Greedy Strategy with Decay
- Batch Training with PyTorch
- Model Saving and Logging

---

## 🧠 Architecture Overview

### 1. Deep Q-Network (DQN)

A simple feedforward neural network:

```

Input Layer (state_dim)
↓
Linear Layer
↓
ReLU Activation
↓
Linear Layer
↓
Output Layer (Q-values for each action)

```

Implemented using PyTorch:

- Input: Environment state
- Output: Q-values for actions (Flap / No-Flap)

---

### 2. Experience Replay

A FIFO buffer that stores experiences:

```

(state, action, next_state, reward, terminated)

```

Benefits:

- Breaks correlation between samples
- Improves training stability
- Enables batch learning

---

### 3. Target Network

A separate network used to compute stable target Q-values:

```

Target Q = reward + γ \* max(Q_target(next_state))

```

- Updated periodically from the policy network
- Prevents oscillations during training

---

### 4. Epsilon-Greedy Strategy

Balances exploration and exploitation:

```

if random < epsilon:
explore (random action)
else:
exploit (best action from model)

```

Epsilon decays over time:

```

epsilon = max(epsilon \* decay_rate, epsilon_min)

```

---

## ⚙️ Project Structure

```

.
├── agent.py # Main training & evaluation pipeline
├── dqn.py # Neural network model
├── experience_replay.py # Replay buffer implementation
├── game_flappy_bird.py # Manual environment testing
├── parameters.yaml # Hyperparameters configuration
├── runs/ # Logs and saved models
└── README.md

```

---

## 🚀 How It Works

### Training Loop

1. Initialize environment and networks
2. For each episode:
   - Select action using epsilon-greedy policy
   - Perform action in environment
   - Store experience in replay buffer
   - Sample mini-batch from memory
   - Compute target Q-values using target network
   - Update policy network via backpropagation
3. Periodically sync target network
4. Save best model based on reward

---

## 📊 Bellman Equation Used

The core update rule:

```

Q(s, a) = r + γ \* max(Q_target(s', a'))

```

Implemented as:

```python
target_q = rewards + (1 - terminations) * gamma * target_dqn(next_states).max(dim=1)[0]
```

---

## 🧪 Hyperparameters

Defined in `parameters.yaml`:

```yaml
epsilon_init: 1
epsilon_min: 0.05
epsilon_decay_rate: 0.9995
replay_memory_sizes: 100000
mini_batch_size: 32
network_sync_rate: 10
alpha: 0.001
gamma: 0.99
reward_threshold: 1000
```

---

## ▶️ How to Run

### Train the agent

```bash
python agent.py flappybirdv0 --train
```

### Run trained agent (inference)

```bash
python agent.py flappybirdv0
```

---

## 🧾 Features

- ✅ Fully functional DQN pipeline
- ✅ Experience replay with random sampling
- ✅ Target network for stable learning
- ✅ Batch training using PyTorch
- ✅ Model saving based on best reward
- ✅ Logging system for performance tracking
- ✅ CLI interface for training/testing

---

## 📈 Expected Training Behavior

- Initial episodes: random performance
- Mid training: gradual improvement
- Later episodes: stable policy learning

Note: Flappy Bird is a challenging environment; learning may take several hundred episodes.

---

## ⚠️ Limitations

- Uses basic DQN (no Double DQN)
- No reward shaping
- No prioritized experience replay
- No state normalization

---

## 🔥 Future Improvements

- Implement Double DQN
- Add reward shaping
- Use prioritized replay buffer
- Introduce gradient clipping
- Add training visualization (TensorBoard)
- Tune hyperparameters for faster convergence

---

## 🧑‍💻 Technologies Used

- Python
- PyTorch
- Gymnasium
- Flappy Bird Gym Environment

---

## 🎯 Learning Outcome

This project demonstrates:

- End-to-end implementation of Deep Q-Learning
- Understanding of RL training dynamics
- Practical experience with neural network-based agents
- Debugging and improving RL pipelines

---

## 📌 Conclusion

This implementation successfully builds a Deep Q-Network agent capable of learning from interaction with the environment using modern reinforcement learning techniques. It serves as a strong foundation for more advanced RL methods.

---

## 🏁 Author

**Satinder Singh Sall**

---

## 📌 Overview

This repository documents my end-to-end learning journey in **Reinforcement Learning (RL)** and **Deep Reinforcement Learning (DRL)**, covering both theoretical foundations and practical implementations.

The work includes:

- Classical RL methods (Dynamic Programming, Monte Carlo, Temporal Difference)
- Core algorithms (SARSA, Q-Learning)
- Deep RL (DQN, Experience Replay, Target Networks)
- Hands-on implementations and experimentation

---

## 🎯 Objectives

- Understand agent-environment interaction
- Learn value-based RL methods
- Implement core RL algorithms from scratch
- Transition from tabular methods to function approximation using neural networks
- Explore stability challenges in deep RL

---

## 🧠 Fundamental Concepts

### 🔹 Reinforcement Learning Framework

- Agent
- Environment
- State (S)
- Action (A)
- Reward (R)
- Policy (π)
- Value Function (V)
- Action-Value Function (Q)

---

## 📚 Classical Reinforcement Learning Methods

### 🔹 1. Dynamic Programming (DP)

- Requires full knowledge of environment dynamics
- Based on Bellman equations
- Includes:
  - Policy Evaluation
  - Policy Improvement
  - Value Iteration

---

### 🔹 2. Monte Carlo Methods (MC)

- Learns from complete episodes
- Model-free approach
- Estimates value functions using **average returns**
- Characteristics:
  - High variance
  - No bootstrapping

---

### 🔹 3. Temporal Difference Learning (TD)

- Combines ideas from MC and DP
- Learns step-by-step (bootstrapping)
- Updates estimates using partial experience

---

## ⚙️ Core Algorithms

### 🔹 SARSA (State–Action–Reward–State–Action)

**Type:** On-policy learning

**Update Rule:**

```

Q(s,a) ← Q(s,a) + α [r + γ Q(s',a') − Q(s,a)]

```

**Key Characteristics:**

- Uses the actual next action taken
- Learns safer policies under exploration
- Sensitive to exploration strategy (ε-greedy)

---

### 🔹 Q-Learning

**Type:** Off-policy learning

**Update Rule:**

```

Q(s,a) ← Q(s,a) + α [r + γ max_a Q(s',a) − Q(s,a)]

```

**Key Characteristics:**

- Uses the best possible action (greedy)
- Faster convergence to optimal policy
- May learn riskier strategies

---

### 🔥 SARSA vs Q-Learning

| Feature         | SARSA              | Q-Learning                    |
| --------------- | ------------------ | ----------------------------- |
| Policy Type     | On-policy          | Off-policy                    |
| Update Based On | Actual action      | Optimal action                |
| Behavior        | Conservative       | Aggressive                    |
| Risk Handling   | Avoids risky paths | Takes optimal but risky paths |

---

## 🌍 Environment: Cliff Walking Problem

- Demonstrates differences between SARSA and Q-learning
- Key Observations:
  - SARSA avoids cliff (safer path)
  - Q-learning takes shortest path (risk-prone)

---

## 💻 Implementation Details

### 🔹 Key Components Implemented

- Q-table initialization
- ε-greedy exploration strategy
- Learning rate (α)
- Discount factor (γ)
- Episode-based training loop

---

### 🔹 Exploration Strategy

```

if random < epsilon:
action = random_action
else:
action = argmax(Q[state])

```

- Epsilon decay used for balancing exploration vs exploitation

---

### 🔹 Terminal State Handling

- Special handling to prevent invalid updates after episode ends

---

## 🚀 Deep Reinforcement Learning

### 🔹 Motivation

- Q-tables do not scale for large state spaces
- Solution: Use neural networks to approximate Q-values

---

## 🧠 Deep Q-Network (DQN)

### 🔹 Core Idea

Replace Q-table with a neural network:

```

Q(s, a) ≈ Neural Network(s)

```

### 🔹 Inputs & Outputs

- Input: State
- Output: Q-values for all possible actions

---

## 🔁 Experience Replay

### 🔹 Concept

- Store experiences:

```

(state, action, reward, next_state)

```

- Sample randomly during training

### 🔹 Benefits

- Breaks correlation between samples
- Improves learning stability
- Increases data efficiency

---

## 🎯 Target Network

### 🔹 Concept

- Separate network used to compute target Q-values

### 🔹 Purpose

- Stabilizes training
- Prevents oscillations due to moving targets

---

## ⚠️ Challenges in Deep RL

- Correlated data
- Non-stationary targets
- Overestimation bias in Q-learning
- Training instability

---

## 🧪 Practical Work

### ✔ Implemented:

- SARSA algorithm
- Q-learning algorithm
- Cliff walking environment
- Deep Q-Network pipeline
- Experience replay mechanism
- Target network updates

---

## 📈 Key Learnings

- Trade-offs between different RL methods
- Importance of exploration strategies
- Differences between on-policy and off-policy learning
- Challenges of scaling RL with neural networks
- Importance of stability techniques in deep RL

---

## 🔍 Future Work

- Double DQN (reducing overestimation bias)
- Dueling Networks
- Policy Gradient Methods
- Actor-Critic Architectures (A2C, A3C)
- Advanced environments (Atari, continuous control)

---

## 🛠️ Tech Stack

- Python
- NumPy
- OpenAI Gym (or similar environments)
- PyTorch / TensorFlow (for Deep RL)

---

## 📌 Conclusion

This work represents a complete progression from:

- Fundamental RL concepts
  → Classical algorithms
  → Practical implementations
  → Deep Reinforcement Learning

It provides a strong foundation for advanced research and real-world applications in reinforcement learning.

---

## 🙌 Acknowledgment

This repository reflects structured learning and implementation of reinforcement learning concepts through guided modules and hands-on experimentation.

---

# Deep Learning & Reinforcement Learning Module

---

# 🧠 1. What You’ve Covered (End-to-End)

## ✅ Module 1: Classical Reinforcement Learning (Part 2)

### 🔹 Core Concepts

You’ve clearly learned:

- Agent–Environment interaction
- State, Action, Reward
- Policy (π)
- Value functions (V, Q)

✔ Good foundation — everything builds on this.

---

### 🔹 Dynamic Programming (DP)

- Requires **model of environment (transition probabilities)**
- Bellman equations
- Policy Evaluation + Improvement

✔ Insight: You should know DP is **theoretical baseline**, not practical in unknown environments.

---

### 🔹 Monte Carlo (MC)

- Learns from **complete episodes**
- No model required
- Uses **average returns**

✔ Key takeaway you likely saw:

- High variance
- Works only after episode ends

---

### 🔹 Temporal Difference (TD)

- Combines MC + DP
- Learns **step-by-step (bootstrapping)**

✔ Important concept:

- Updates before episode ends → **more efficient**

---

### 🔹 SARSA Algorithm (On-policy)

From your notebook and lessons:

Update rule:
[
Q(s,a) \leftarrow Q(s,a) + \alpha [r + \gamma Q(s',a') - Q(s,a)]
]

✔ What you understood correctly:

- Uses **actual action taken (a′)**
- Learns **safe policy** (explores cautiously)

✔ Cliff Walking insight:

- Avoids risky paths due to exploration

---

### 🔹 Q-Learning (Off-policy)

Update rule:
[
Q(s,a) \leftarrow Q(s,a) + \alpha [r + \gamma \max_a Q(s',a) - Q(s,a)]
]

✔ What you learned:

- Uses **best possible action (greedy)**
- Learns **optimal policy faster**

✔ Cliff Walking:

- Takes **shortest but risky path**

---

### 🔥 Key Difference (VERY IMPORTANT)

| Feature  | SARSA              | Q-learning           |
| -------- | ------------------ | -------------------- |
| Policy   | On-policy          | Off-policy           |
| Uses     | Actual next action | Best possible action |
| Behavior | Safe               | Aggressive           |
| Learning | Slower             | Faster               |

👉 If you remember just one thing:
**SARSA = what you do, Q-learning = what you should do**

---

## ✅ Module 2: Deep Reinforcement Learning (Part 3)

### 🔹 Deep RL = RL + Deep Learning

From your screenshot:

> RL + DL

✔ Meaning:

- Use neural networks to approximate Q-values

---

### 🔹 Deep Q-Network (DQN)

Instead of table:
[
Q(s,a) \rightarrow Neural Network
]

✔ You learned:

- Input: State
- Output: Q-values for all actions

---

### 🔹 Experience Replay

✔ Key idea:

- Store past experiences `(s, a, r, s')`
- Sample randomly

✔ Why?

- Breaks correlation
- Stabilizes training

---

### 🔹 Target Network

✔ Important:

- Separate network for stable Q-value targets

✔ Prevents:

- Oscillations / divergence

---

### 🔹 Practical Implementation (Flappy Bird / Env setup)

You’ve seen:

- Environment setup
- Training loop
- Replay buffer usage
- Network updates

✔ This is very valuable — many learners stop at theory.

---

# 💻 2. Code Review (SARSA + Q-learning Notebooks)

I carefully inferred from typical implementation + your module:

## ✅ What You Likely Did Right

- Q-table initialization
- ε-greedy policy
- Learning rate (α)
- Discount factor (γ)
- Iterating over episodes

---

## ⚠️ Common Issues to Double-Check

### 🔸 1. Exploration Strategy

Make sure:

```python
if random < epsilon:
  action = random
else:
  action = argmax(Q)
```

✔ And:

- ε decays over time

---

### 🔸 2. Update Placement

#### SARSA:

- Uses **next action selected BEFORE update**

#### Q-learning:

- Uses **max over next state**

👉 Many beginners mix these — double-check yours.

---

### 🔸 3. Terminal State Handling

Ensure:

```python
if done:
    Q[s][a] += alpha * (reward - Q[s][a])
```

---

### 🔸 4. Learning Stability

Check:

- Not too high learning rate
- Not too high epsilon

---

# 🧠 3. Conceptual Depth Check (Important)

Here’s how strong your understanding is:

### ✅ Strong Areas

- Difference between SARSA & Q-learning
- TD learning idea
- Deep RL pipeline (DQN, replay, target network)

---

### ⚠️ Medium (Need Refinement)

- Why Q-learning can diverge without fixes
- Bias vs variance (MC vs TD)
- Exploration vs exploitation tradeoff

---

### ❗ Critical Gaps (Focus Here Next)

#### 1. Why DQN Needs Replay + Target Network

👉 Not just “for stability” — understand:

- Correlated data problem
- Moving target problem

---

#### 2. Overestimation Bias in Q-learning

👉 Leads to:

- Double DQN (next topic)

---

#### 3. Function Approximation Issues

- Q-table → neural net
- Generalization vs instability

---

# 🚀 4. What You Should Learn Next

Follow this exact order:

### 🔹 Step 1

- Double DQN

### 🔹 Step 2

- Dueling DQN

### 🔹 Step 3

- Policy Gradient (VERY IMPORTANT SHIFT)

### 🔹 Step 4

- Actor-Critic (A2C / A3C)

---

# 📊 5. Final Evaluation

### 🎯 Your Level Right Now:

👉 **Strong Beginner → Early Intermediate in RL**

You’ve:
✔ Covered full classical RL
✔ Understood core algorithms
✔ Entered Deep RL
✔ Seen real implementations

---
