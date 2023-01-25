

# 对上一笔记中的value分析，确定策略函数


import gymnasium as gym
import random
from tqdm import tqdm


env = gym.make('Blackjack-v1', natural=False, sab=False, render_mode='rgb_array')


episode = 20000

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
value_with_action = defaultdict(list)  # value（state）
Q_table = defaultdict(lambda: [0, 0])


for t in trajectories:

    visited = set()
    for (s, a, r) in t[::-1]:
        if s not in visited:  # 只添加新的，见过的不添加，即不要循环
            G = r + gamma * G
            value_with_action[(s, a)].append(G)
            visited.add(s)
            # print(value)

for [s, a], Vs in value_with_action.items():
    Q_table[s][a] = np.mean(Vs)
print(Q_table)


# 基本策略，每次返回最大值  （理解思路，实际不用）
def basic_policy(state):
    global Q_table

    return np.argmax(Q_table[state])
# print(basic_policy(1))


# 常用策略，在返回最大值的基础上，可以偶尔随机返回其他值
def policy(state, episode=0.2):
    global Q_table

    if random.random() < episode:
        return np.random.choice(range(len(Q_table[state])))
    else:
        return np.argmax(Q_table[state])



