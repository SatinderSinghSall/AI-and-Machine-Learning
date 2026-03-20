from collections import deque
import random

class ReplayMemory():
    # Create FIFO Queue: Experience Replay
    def __init__(self, maxlen, seed = None):
        self.memory = deque([], maxlen = maxlen)

    # Adding Elements:
    def append(self, new_exp):
        self.memory.append(new_exp)

    # Extracting Random Samples:
    def sample(self, sample_size):
        return random.sample(self, self.memory, sample_size)

    # Calculating the Length: Current Buffer Size
    def __init__(self):
        return len(self.memory)
