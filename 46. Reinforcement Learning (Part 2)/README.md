# AI / ML: Deep Learning – 46. Reinforcement Learning (Part 2)

# Deep Learning & Reinforcement Learning Module

# 1. Topics Covered in Your Module

From the sidebar in your screenshots, the module **“Reinforcement Learning (Part 2)”** includes:

1. Diverse RL Methods
2. Dynamic Programming
3. Monte Carlo Methods
4. Temporal Difference (TD) Learning
5. SARSA Algorithm
6. Q-Learning Algorithm
7. Cliff Walking Problem & Environment
8. SARSA Implementation
9. What Agent Learns with SARSA
10. Cliff Walking (SARSA) Code
11. Q-Learning Implementation
12. What Agent Learns with Q-Learning
13. Cliff Walking (Q-Learning) Code
14. Class Slides

So the module structure is:

**RL Methods → TD Learning → On-policy (SARSA) → Off-policy (Q-Learning) → Environment experiment**

This is the **standard progression used in RL textbooks**.

---

# 2. Environment Used

Both notebooks use the same environment:

```
CliffWalking-v1
```

From **Gymnasium**.

### Environment Properties

```
env.observation_space.n = 48
env.action_space.n = 4
```

Meaning:

| Component | Meaning       |
| --------- | ------------- |
| States    | 48 grid cells |
| Actions   | 4 directions  |

Actions:

```
0 = UP
1 = RIGHT
2 = DOWN
3 = LEFT
```

Grid layout (4 × 12):

```
S . . . . . . . . . . .
. . . . . . . . . . . .
. . . . . . . . . . . .
. C C C C C C C C C C G
```

S = start
G = goal
C = cliff (fall → reward = −100)

Normal step reward = **−1**

---

# 3. Hyperparameters Used

Both algorithms use the same learning parameters:

```
gamma = 0.99
alpha = 0.5
epsilon = 0.1
episodes = 500
```

### Meaning

| Parameter | Purpose                 |
| --------- | ----------------------- |
| gamma     | discount factor         |
| alpha     | learning rate           |
| epsilon   | exploration probability |
| episodes  | training iterations     |

---

# 4. Q-Table Initialization

```
Q = np.zeros((48, 4))
```

Meaning:

```
Q[state][action]
```

Example:

```
Q[36][2]
```

Expected reward if agent:

```
state = 36
action = DOWN
```

---

# 5. Exploration Policy (Epsilon Greedy)

Your notebook defines:

```
def epsilon_greedy(state):
    if random.random() < epsilon:
        return env.action_space.sample()
    else:
        return np.argmax(Q[state])
```

Logic:

```
10% → random action (explore)
90% → best action (exploit)
```

This prevents the agent from getting stuck in **local optimum policies**.

---

# 6. SARSA Algorithm (On-Policy)

You studied **SARSA first**.

SARSA stands for:

```
State
Action
Reward
State
Action
```

Update rule:

Q(s,a) \leftarrow Q(s,a) + \alpha \left[r + \gamma Q(s',a') - Q(s,a)\right]

### Meaning

The next action **a'** is chosen using the **same policy**.

So SARSA learns from the **actual action taken**.

---

### SARSA Training Flow

```
for episode:
    state = reset()

    action = epsilon_greedy(state)

    while not done:
        next_state, reward, done = env.step(action)

        next_action = epsilon_greedy(next_state)

        update Q-table

        state = next_state
        action = next_action
```

Key point:

```
SARSA uses the action chosen by policy
```

So it is **on-policy learning**.

---

# 7. Q-Learning Algorithm (Off-Policy)

Your second notebook implements **Q-Learning**.

Update rule:

Q(s,a) \leftarrow Q(s,a) + \alpha \left[r + \gamma \max_{a'} Q(s',a') - Q(s,a)\right]

Key difference:

```
max Q(s',a')
```

Instead of using the **next action from policy**, it assumes the **best possible action**.

Thus:

```
Q-learning = off-policy
```

---

# 8. Training Loop Structure (Your Code)

Both notebooks follow this pattern:

```
for episode in range(episodes):

    render = (episode % 50 == 0)

    if render:
        env = gym.make(... render_mode="human")
    else:
        env = gym.make(...)
```

This means:

Every **50 episodes** you visualize training.

This helps see the **agent improving over time**.

---

# 9. Testing the Learned Policy

After training, both notebooks test the agent:

```
state, _ = env.reset()
done = False

while not done:
    action = np.argmax(Q[state])
    next_state, reward, done, _, _ = env.step(action)
```

This means:

```
Policy = greedy
```

The agent now follows the **best learned action**.

---

# 10. Q-Table Inspection

Your notebook checks values like:

```
Q[36]
Q[35]
```

Example output might look like:

```
Q[36] = [-12, -11, -10, -13]
```

Meaning:

```
Best action = argmax(Q[36])
```

The agent learned which move gives the **highest long-term reward**.

---

# 11. Cliff Walking Behavior

This environment demonstrates the **difference between SARSA and Q-Learning**.

### SARSA Agent

Policy:

```
Safe path
```

Because SARSA accounts for exploration risk.

Example path:

```
S → up → safe route → G
```

### Q-Learning Agent

Policy:

```
Shortest path near cliff
```

Because it assumes **optimal future actions**.

Example:

```
S → right along cliff → G
```

This path is risky but shorter.

---

# 12. Major Concepts You Learned

This module covers **core reinforcement learning concepts**.

### 1️⃣ Dynamic Programming

Used when:

```
model of environment is known
```

Examples:

```
Policy Iteration
Value Iteration
```

---

### 2️⃣ Monte Carlo Methods

Learning using **complete episodes**.

Update after episode ends.

Pros:

```
No model needed
```

Cons:

```
High variance
```

---

### 3️⃣ Temporal Difference Learning

TD combines:

```
Monte Carlo + Dynamic Programming
```

Key idea:

```
update after every step
```

TD error:

```
δ = r + γV(s') − V(s)
```

---

### 4️⃣ SARSA

```
On-policy
```

Learns **policy actually executed**.

Safer behaviour.

---

### 5️⃣ Q-Learning

```
Off-policy
```

Learns **optimal policy regardless of exploration**.

More aggressive behaviour.

---

# 13. Summary of Algorithms

| Algorithm           | Type          | Update Target  |
| ------------------- | ------------- | -------------- |
| Dynamic Programming | Model-based   | exact value    |
| Monte Carlo         | Model-free    | episode return |
| TD Learning         | Model-free    | step update    |
| SARSA               | On-policy TD  | Q(s', a')      |
| Q-Learning          | Off-policy TD | max Q(s',a')   |

---

# 14. What You Achieved in This Module

By the end of this module you now understand:

✔ RL environment interaction
✔ Exploration vs exploitation
✔ Q-tables
✔ Epsilon-greedy policies
✔ Temporal difference learning
✔ On-policy vs Off-policy learning
✔ Cliff Walking environment
✔ SARSA vs Q-Learning behavior

These are **core foundations of reinforcement learning**.

---

# 15. Important Insight (Very Useful for Interviews)

Difference between SARSA and Q-learning:

| Feature  | SARSA                   | Q-Learning      |
| -------- | ----------------------- | --------------- |
| Policy   | On-policy               | Off-policy      |
| Update   | Q(s',a')                | max Q(s',a')    |
| Behavior | Safe                    | Risky           |
| Example  | Cliff Walking safe path | Cliff edge path |

---

✅ **Conclusion:**
Your module is a **correct and well-structured introduction to RL control algorithms** using Gymnasium environments.

You now have the foundations needed for:

```
Deep Q Networks (DQN)
Policy Gradient
Actor-Critic
PPO
RLHF
```

---
