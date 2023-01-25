

# 随机方式玩十万次21点并记录，然后用蒙特卡罗方法计算value值，在value值的基础上设置策略
# 随后在策略指导下再次开始玩一万次21点，最后统计胜率


import gymnasium as gym
import random
from tqdm import tqdm


env = gym.make('Blackjack-v1', natural=False, sab=False, render_mode='rgb_array')


episode = 100000

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
# print(Q_table)


# 常用策略，在返回最大值的基础上，可以偶尔随机返回其他值
def policy(state, episode=0.2):
    global Q_table

    if random.random() < episode:
        return np.random.choice(range(len(Q_table[state])))
    else:
        return np.argmax(Q_table[state])


# 用上面的策略玩21点游戏，并查看胜率
# env = gym.make('Blackjack-v1', natural=False, sab=False, render_mode='rgb_array')

episode = 10000

state, info = env.reset()

trajectories = []

win_or_lose = []  # 增加胜率统计

for _ in tqdm(range(episode)):
    trajectory = []
    while True:
        action = policy(state)
        next_state, reward, terminated, truncated, info = env.step(action)

        trajectory.append((state, action, reward))

        state = next_state

        if terminated or truncated:
            if reward > 0:
                win_or_lose.append(1)
            else:
                win_or_lose.append(0)

            state, info = env.reset()

            trajectories.append(trajectory)

            break

env.close()


win_percentage = sum(win_or_lose) / len(win_or_lose)
print(win_percentage)






