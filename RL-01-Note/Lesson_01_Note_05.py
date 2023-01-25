
# gymnasium示例


import gymnasium as gym
from tqdm import tqdm


env = gym.make('Blackjack-v1', natural=False, sab=False, render_mode='rgb_array')


episode = 100

state, info = env.reset()

for _ in tqdm(range(episode)):
    while True:
        action = env.action_space.sample()
        next_state, reward, terminated, truncated, info = env.step(action)

        state = next_state

        if terminated or truncated:
            state, info = env.reset()
            break

env.close()













