import flappy_bird_gymnasium
import gymnasium as gym
from dqn import DQN
from experience_replay import ReplayMemory
import itertools
import yaml
import torch
import torch.nn as nn
import torch.optim as optim
import random

# Device setup
if torch.backends.mps.is_available():
    device = "mps"
elif torch.cuda.is_available():
    device = "cuda"
else:
    device = "cpu"


class Agent:
    def __init__(self, params_set):
        self.params_set = params_set

        # Load parameters
        with open("parameters.yaml", "r") as f:
            all_param_set = yaml.safe_load(f)
            params = all_param_set[params_set]

        self.alpha = params["alpha"]
        self.gamma = params["gamma"]

        self.epsilon_init = params["epsilon_init"]
        self.epsilon_min = params["epsilon_min"]
        self.epsilon_decay_rate = params["epsilon_decay_rate"]

        self.replay_memory_sizes = params["replay_memory_sizes"]
        self.mini_batch_size = params["mini_batch_size"]

        self.network_sync_rate = params["network_sync_rate"]
        self.reward_threshold = params["reward_threshold"]

        self.loss_fn = nn.MSELoss()
        self.optimizer = None

    def run(self, is_training=True, render=False):
        env = gym.make("FlappyBird-v0", render_mode="human" if render else None)

        num_states = env.observation_space.shape[0]
        num_actions = env.action_space.n

        policy_dqn = DQN(num_states, num_actions).to(device)

        if is_training:
            memory = ReplayMemory(self.replay_memory_sizes)
            epsilon = self.epsilon_init

            target_dqn = DQN(num_states, num_actions).to(device)
            target_dqn.load_state_dict(policy_dqn.state_dict())

            steps = 0
            self.optimizer = optim.Adam(policy_dqn.parameters(), lr=self.alpha)

        for episode in itertools.count():
            state, _ = env.reset()
            state = torch.tensor(state, dtype=torch.float32, device=device)

            episode_rewards = 0
            terminated = False

            while not terminated:
                # Epsilon-greedy action
                if is_training and random.random() < epsilon:
                    action = torch.tensor(
                        env.action_space.sample(),
                        dtype=torch.long,
                        device=device
                    )
                else:
                    with torch.no_grad():
                        action = policy_dqn(state.unsqueeze(0)).argmax(dim=1)

                # Step environment
                next_state, reward, terminated, _, _ = env.step(action.item())

                next_state = torch.tensor(next_state, dtype=torch.float32, device=device)
                reward = torch.tensor(reward, dtype=torch.float32, device=device)

                episode_rewards += reward.item()

                if is_training:
                    memory.append(state, action, next_state, reward, terminated)
                    steps += 1

                state = next_state

            print(f"Episode: {episode + 1} | Reward: {episode_rewards:.2f} | Epsilon: {epsilon:.4f}")

            if is_training:
                # Decay epsilon
                epsilon = max(epsilon * self.epsilon_decay_rate, self.epsilon_min)

                # Train
                if len(memory) >= self.mini_batch_size:
                    mini_batch = memory.sample(self.mini_batch_size)
                    self.optimize(mini_batch, policy_dqn, target_dqn)

                # Sync target network
                if steps >= self.network_sync_rate:
                    target_dqn.load_state_dict(policy_dqn.state_dict())
                    steps = 0

    def optimize(self, mini_batch, policy_dqn, target_dqn):
        states, actions, next_states, rewards, terminations = zip(*mini_batch)

        states = torch.stack(states)
        actions = torch.stack(actions)
        next_states = torch.stack(next_states)
        rewards = torch.stack(rewards)
        terminations = torch.tensor(terminations, dtype=torch.float32, device=device)

        # Target Q-values
        with torch.no_grad():
            target_q = rewards + (1 - terminations) * self.gamma * \
                       target_dqn(next_states).max(dim=1)[0]

        # Current Q-values
        current_q = policy_dqn(states).gather(
            dim=1,
            index=actions.unsqueeze(1)
        ).squeeze()

        # Loss
        loss = self.loss_fn(current_q, target_q)

        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
