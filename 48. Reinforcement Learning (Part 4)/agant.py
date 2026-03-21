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

if torch.backend.mps.is_available():
    device = "mps"
elif torch.cuda.is_available():
    device = "cuda"
else:
    device = "cpu"

class Agent:
    def __init__(self, params_set):
        self.params_set = params_set

        with open("parameters.yaml", "r") as f:
            all_param_set = yaml.safe_load(f)
            params = all_param_set(params_set)

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

    def run(self, is_training = True, render = False):
        env = gym.make("FlappyBird-v0", render_mode="human" if render else None)

        num_states = env.observation_space.shape[0] # input dim
        num_actions = env.action_space.n # output dim

        policy_dqn = DQN(num_states, num_actions).to(device)

        if is_training:
            memory = ReplayMemory(self.replay_memory_sizes)
            epsilon = self.epsilon_init

        for episode in itertools.count():
            state, _ = env.reset()
            state = torch.tensor(state, dtype=torch.float, device=device)

            episode_rewards = 0
            terminated = False

            obs, _ = env.reset()
            while not terminated:
                if is_training and random.random() < epsilon:
                    # Next action:
                    # (feed the observation to your agent here)
                    action = env.action_space.sample() # Explore
                    action = torch.tensor(state, dtype = torch.long, device = device)
                else:
                    with torch.no_grad():
                        action = policy_dqn(state.unsqueeze(dim=0)).squeeze().argmax() # Exploit

                # Processing: terminated => done
                next_state, reward, terminated, _, _ = env.step(action)

                # Create Tensors:
                reward = torch.tensor(reward, dtype=torch.float, device=device)
                next_state = torch.tensor(next_state, dtype=torch.float, device=device)

                if is_training:
                    memory.append(state, action, next_state, reward, terminated)

                # Checking if the player is still alive
                if terminated:
                    break

                state = next_state
                episode_rewards = episode_rewards + reward

            print(f"Episode: {episode + 1} with Total Reward: {episode_rewards} & Epsilon: {epsilon}")
            
            # Epsilon Decay:
            epsilon = max(epsilon * self.decay, self.epsilon_min)

            # env.close() # Commented to manually stop the training.
