

# 用gymnasium里的21点游戏示例，求value示例


import gymnasium as gym
from tqdm import tqdm


env = gym.make('Blackjack-v1', natural=False, sab=False, render_mode='rgb_array')


episode = 1000

state, info = env.reset()

trajectories = []

for _ in tqdm(range(episode)):
    trajectory = []
    while True:
        action = env.action_space.sample()
        next_state, reward, terminated, truncated, info = env.step(action)

        trajectory.append((state, action, reward))

        state = next_state

        if terminated or truncated:
            state, info = env.reset()

            trajectories.append(trajectory)

            break

env.close()

# print(trajectories)
# print('one sample of trajectories : ')
# print(trajectories[2])


# 用蒙特卡罗方法求value
import numpy as np
from collections import defaultdict

G = 0  # 单步reward
gamma = 0.9
value = defaultdict(list)  # value（state）
for t in trajectories:
    for (s, a, r) in t[::-1]:
        G = r + gamma * G
        value[s].append(G)
        # print(value)


for s, g in value.items():
    value[s] = np.mean(g)

print(value)








