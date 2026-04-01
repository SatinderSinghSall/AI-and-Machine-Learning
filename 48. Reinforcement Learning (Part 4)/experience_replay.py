from collections import deque
import random

class ReplayMemory:
    # Create FIFO Queue: Experience Replay
    def __init__(self, maxlen):
        self.memory = deque(maxlen=maxlen)

    # Adding Elements:
    def append(self, state, action, next_state, reward, terminated):
        self.memory.append((state, action, next_state, reward, terminated))

    # Extracting Random Samples:
    def sample(self, sample_size):
        return random.sample(self.memory, sample_size)

    # Calculating the Length: Current Buffer Size
    def __len__(self):
        return len(self.memory)